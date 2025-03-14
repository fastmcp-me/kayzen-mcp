import axios, { AxiosRequestConfig } from 'axios';
import dotenv from 'dotenv';

dotenv.config();

export interface KayzenConfig {
  userName: string;
  password: string;
  basicAuthToken: string;
  baseUrl: string;
}

interface AuthResponse {
  access_token: string;
}

export class KayzenClient {
  private baseUrl: string;
  private userName: string;
  private password: string;
  private basicAuthToken: string;
  private authToken: string | null = null;
  private tokenExpiry: Date | null = null;

  constructor() {
    const baseUrl = process.env.KAYZEN_BASE_URL;
    const userName = process.env.KAYZEN_USERNAME;
    const password = process.env.KAYZEN_PASSWORD;
    const basicAuthToken = process.env.KAYZEN_BASIC_AUTH;

    if (!userName || !password || !basicAuthToken) {
      throw new Error('KAYZEN_USERNAME, KAYZEN_PASSWORD, and KAYZEN_BASIC_AUTH must be set in environment variables');
    }

    this.baseUrl = baseUrl || 'https://api.kayzen.io/v1';
    this.userName = userName;
    this.password = password;
    this.basicAuthToken = basicAuthToken;
  }

  private async getAuthToken(): Promise<string> {
    if (this.authToken && this.tokenExpiry && new Date() < this.tokenExpiry) {
      return this.authToken;
    }

    const url = `${this.baseUrl}/authentication/token`;
    const payload = {
      grant_type: 'password',
      username: this.userName,
      password: this.password
    };
    const headers = {
      accept: 'application/json',
      'content-type': 'application/json',
      authorization: `Basic ${this.basicAuthToken}`
    };

    try {
      const response = await axios.post<AuthResponse>(url, payload, { headers });
      this.authToken = response.data.access_token;
      this.tokenExpiry = new Date(Date.now() + 25 * 60 * 1000);
      return this.authToken;
    } catch (error) {
      console.error('Error getting auth token:', error);
      throw error;
    }
  }

  private async makeRequest<T>(method: string, endpoint: string, params: Record<string, unknown> = {}) {
    const token = await this.getAuthToken();
    const config: AxiosRequestConfig = {
      method,
      url: `${this.baseUrl}${endpoint}`,
      headers: {
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
      },
      params
    };

    try {
      const response = await axios<T>(config);
      return response.data;
    } catch (error) {
      console.error(`Error making request to ${endpoint}:`, error);
      throw error;
    }
  }

  async listReports() {
    return this.makeRequest('GET', '/reports');
  }

  async getReportResults(reportId: string, startDate?: string, endDate?: string) {
    const params: Record<string, string> = {};
    if (startDate) params.start_date = startDate;
    if (endDate) params.end_date = endDate;

    return this.makeRequest('GET', `/reports/${reportId}/report_results`, params);
  }
}
