import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AiAssistantService } from '../services/ai-assistant.service';

@Component({
  selector: 'app-ai-assistant',
  templateUrl: './ai-assistant.component.html',
  styleUrls: ['./ai-assistant.component.css']
})
export class AiAssistantComponent implements OnInit {
  form: FormGroup;
  loading = false;
  error: string | null = null;
  








  constructor(
    private fb: FormBuilder,
    private router: Router,
    private service: AiAssistantService
  ) {
    this.form = this.fb.group({

      name: ['', Validators.required],

      relevant: ['', []],

      helpful_responses: ['', []],

    });
  }

  ngOnInit(): void {
    // Component initialization
  }

  onSubmit(): void {
    if (this.form.invalid) {
      return;
    }

    this.loading = true;
    this.error = null;

    this.service.create(this.form.value).subscribe({
      next: (response) => {
        console.log('Success:', response);
        // Navigate on success
        this.router.navigate(['/ai-assistants']);
      },
      error: (error) => {
        console.error('Error:', error);
        this.error = error.message || 'An error occurred';
        this.loading = false;
      },
      complete: () => {
        this.loading = false;
      }
    });
  }

  onCancel(): void {
    this.router.navigate(['/ai-assistants']);
  }
}