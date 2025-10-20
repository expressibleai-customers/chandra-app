import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { CareProviderPortal } from '../models/care-provider-portal.model';

@Injectable({
  providedIn: 'root'
})
export class CareProviderPortalService {
  private apiUrl = '/api/care_provider_portals';

  constructor(private http: HttpClient) {}

  create(data: Partial<CareProviderPortal>): Observable<CareProviderPortal> {
    return this.http.post<CareProviderPortal>(this.apiUrl, data);
  }

  getAll(): Observable<CareProviderPortal[]> {
    return this.http.get<CareProviderPortal[]>(this.apiUrl);
  }

  getById(id: number): Observable<CareProviderPortal> {
    return this.http.get<CareProviderPortal>(`${this.apiUrl}/${id}`);
  }

  update(id: number, data: Partial<CareProviderPortal>): Observable<CareProviderPortal> {
    return this.http.put<CareProviderPortal>(`${this.apiUrl}/${id}`, data);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}