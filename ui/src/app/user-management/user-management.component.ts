import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserManagementService } from '../services/user-management.service';

@Component({
  selector: 'app-user-management',
  templateUrl: './user-management.component.html',
  styleUrls: ['./user-management.component.css']
})
export class UserManagementComponent implements OnInit {
  form: FormGroup;
  loading = false;
  error: string | null = null;
  


  roleOptions = [{"label": "Caregiver", "value": "caregiver"}, {"label": "Care Receiver", "value": "care_receiver"}, {"label": "Care Provider", "value": "care_provider"}, {"label": "Business/Organization", "value": "business"}];



  constructor(
    private fb: FormBuilder,
    private router: Router,
    private service: UserManagementService
  ) {
    this.form = this.fb.group({

      role: ['', Validators.required],

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
        this.router.navigate(['/user-managements']);
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
    this.router.navigate(['/user-managements']);
  }
}