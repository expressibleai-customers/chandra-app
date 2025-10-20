import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CommunityPlatform } from '../models/community-platform.model';

@Injectable({
  providedIn: 'root'
})
export class CommunityPlatformService {
  private apiUrl = '/api/community_platforms';

  constructor(private http: HttpClient) {}

  create(data: Partial<CommunityPlatform>): Observable<CommunityPlatform> {
    return this.http.post<CommunityPlatform>(this.apiUrl, data);
  }

  getAll(): Observable<CommunityPlatform[]> {
    return this.http.get<CommunityPlatform[]>(this.apiUrl);
  }

  getById(id: number): Observable<CommunityPlatform> {
    return this.http.get<CommunityPlatform>(`${this.apiUrl}/${id}`);
  }

  update(id: number, data: Partial<CommunityPlatform>): Observable<CommunityPlatform> {
    return this.http.put<CommunityPlatform>(`${this.apiUrl}/${id}`, data);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}