import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { CommunityPlatformService } from '../services/community-platform.service';

@Component({
  selector: 'app-community-platform',
  templateUrl: './community-platform.component.html',
  styleUrls: ['./community-platform.component.css']
})
export class CommunityPlatformComponent implements OnInit {
  form: FormGroup;
  loading = false;
  error: string | null = null;
  






  constructor(
    private fb: FormBuilder,
    private router: Router,
    private service: CommunityPlatformService
  ) {
    this.form = this.fb.group({

      community_management: ['', []],

      moderation_tools: ['', []],

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
        this.router.navigate(['/community-platforms']);
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
    this.router.navigate(['/community-platforms']);
  }
}