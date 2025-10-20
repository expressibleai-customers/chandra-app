import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ResourceManagementService } from '../services/resource-management.service';

@Component({
  selector: 'app-resource-management',
  templateUrl: './resource-management.component.html',
  styleUrls: ['./resource-management.component.css']
})
export class ResourceManagementComponent implements OnInit {
  form: FormGroup;
  loading = false;
  error: string | null = null;
  








  constructor(
    private fb: FormBuilder,
    private router: Router,
    private service: ResourceManagementService
  ) {
    this.form = this.fb.group({

      filtering: ['', []],

      categorization: ['', []],

      content_management_capabilities: ['', []],

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
        this.router.navigate(['/resource-managements']);
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
    this.router.navigate(['/resource-managements']);
  }
}