import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserManagement } from '../models/user-management.model';

@Injectable({
  providedIn: 'root'
})
export class UserManagementService {
  private apiUrl = '/api/user_managements';

  constructor(private http: HttpClient) {}

  create(data: Partial<UserManagement>): Observable<UserManagement> {
    return this.http.post<UserManagement>(this.apiUrl, data);
  }

  getAll(): Observable<UserManagement[]> {
    return this.http.get<UserManagement[]>(this.apiUrl);
  }

  getById(id: number): Observable<UserManagement> {
    return this.http.get<UserManagement>(`${this.apiUrl}/${id}`);
  }

  update(id: number, data: Partial<UserManagement>): Observable<UserManagement> {
    return this.http.put<UserManagement>(`${this.apiUrl}/${id}`, data);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}