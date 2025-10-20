import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ResourceManagement } from '../models/resource-management.model';

@Injectable({
  providedIn: 'root'
})
export class ResourceManagementService {
  private apiUrl = '/api/resource-managements';

  constructor(private http: HttpClient) {}

  create(data: Partial<ResourceManagement>): Observable<ResourceManagement> {
    return this.http.post<ResourceManagement>(this.apiUrl, data);
  }

  getAll(): Observable<ResourceManagement[]> {
    return this.http.get<ResourceManagement[]>(this.apiUrl);
  }

  getById(id: number): Observable<ResourceManagement> {
    return this.http.get<ResourceManagement>(`${this.apiUrl}/${id}`);
  }

  update(id: number, data: Partial<ResourceManagement>): Observable<ResourceManagement> {
    return this.http.put<ResourceManagement>(`${this.apiUrl}/${id}`, data);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}