from datetime import datetime
import httpx
from config import config
from typing import Optional, Dict, Any

class KayzenClient:
    def __init__(self):
        self.base_url = config.base_url
        self.api_key = config.api_key
        self.api_secret = config.api_secret
        self.auth_token: Optional[str] = None
        self.token_expiry: Optional[datetime] = None

    async def _get_auth_token(self) -> str:
        """Get or refresh authentication token"""
        if self.auth_token and self.token_expiry and datetime.now() < self.token_expiry:
            return self.auth_token

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/auth/token",
                json={
                    "api_key": self.api_key,
                    "api_secret": self.api_secret
                }
            )
            response.raise_for_status()
            data = response.json()
            self.auth_token = data["token"]
            # Token expires in 24 hours, but we'll refresh after 23 hours
            self.token_expiry = datetime.now().replace(hour=23)
            return self.auth_token

    async def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        """Make authenticated request to Kayzen API"""
        token = await self._get_auth_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        kwargs["headers"] = headers

        async with httpx.AsyncClient() as client:
            response = await client.request(
                method,
                f"{self.base_url}{endpoint}",
                **kwargs
            )
            response.raise_for_status()
            return response.json()

    async def create_report(self, report_type: str, start_date: str, end_date: str,
                          dimensions: list[str], metrics: list[str]) -> Dict[str, Any]:
        """Create a new report"""
        payload = {
            "report_type": report_type,
            "start_date": start_date,
            "end_date": end_date,
            "dimensions": dimensions,
            "metrics": metrics
        }
        return await self._make_request("POST", "/reports", json=payload)

    async def get_report_results(self, report_id: str) -> Dict[str, Any]:
        """Get report results"""
        return await self._make_request("GET", f"/reports/{report_id}/results")

    async def get_report_status(self, report_id: str) -> Dict[str, Any]:
        """Get report status"""
        return await self._make_request("GET", f"/reports/{report_id}/status")
