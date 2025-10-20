import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CareProviderPortalService } from '../services/care-provider-portal.service';

@Component({
  selector: 'app-care-provider-portal',
  templateUrl: './care-provider-portal.component.html',
  styleUrls: ['./care-provider-portal.component.css']
})
export class CareProviderPortalComponent implements OnInit {
  form: FormGroup;
  loading = false;
  error: string | null = null;
  






  constructor(
    private fb: FormBuilder,
    private router: Router,
    private service: CareProviderPortalService
  ) {
    this.form = this.fb.group({

      caregivers: ['', []],

      care_receivers: ['', []],

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
        this.router.navigate(['/care-provider-portals']);
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
    this.router.navigate(['/care-provider-portals']);
  }
}