import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AiAssistant } from '../models/ai-assistant.model';

@Injectable({
  providedIn: 'root'
})
export class AiAssistantService {
  private apiUrl = '/api/ai_assistants';

  constructor(private http: HttpClient) {}

  create(data: Partial<AiAssistant>): Observable<AiAssistant> {
    return this.http.post<AiAssistant>(this.apiUrl, data);
  }

  getAll(): Observable<AiAssistant[]> {
    return this.http.get<AiAssistant[]>(this.apiUrl);
  }

  getById(id: number): Observable<AiAssistant> {
    return this.http.get<AiAssistant>(`${this.apiUrl}/${id}`);
  }

  update(id: number, data: Partial<AiAssistant>): Observable<AiAssistant> {
    return this.http.put<AiAssistant>(`${this.apiUrl}/${id}`, data);
  }

  delete(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}