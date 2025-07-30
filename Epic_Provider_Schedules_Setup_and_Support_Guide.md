# Provider Schedules Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 8A9E2F3D-1B5C-4D7E-9F8A-3C6E9B2D4F7A

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Provider Schedule Templates](#provider-schedule-templates)
  - [Create Provider Schedule Templates](#create-provider-schedule-templates)
  - [Configure Block Types for Different Appointment Types](#configure-block-types-for-different-appointment-types)
  - [Set Up Recurring Schedule Patterns](#set-up-recurring-schedule-patterns)
  - [Manage Provider Availability and Time Off](#manage-provider-availability-and-time-off)
- [Schedule Template Management](#schedule-template-management)
  - [Copy and Modify Existing Templates](#copy-and-modify-existing-templates)
  - [Share Templates Across Providers](#share-templates-across-providers)
  - [Version Control for Template Changes](#version-control-for-template-changes)
- [Advanced Scheduling Features](#advanced-scheduling-features)
  - [Configure Double Booking Rules](#configure-double-booking-rules)
  - [Set Up Block Release Schedules](#set-up-block-release-schedules)
  - [Implement Schedule Optimization](#implement-schedule-optimization)

## Overview

Provider schedules form the foundation of effective appointment scheduling in Epic. This guide covers the setup and management of provider schedule templates, which define when providers are available, what types of appointments they can accommodate, and how their time is allocated across different patient populations and visit types.

## Provider Schedule Templates

### Create Provider Schedule Templates

Provider schedule templates define the recurring pattern of availability for each provider:

**Template Components:**
1. **Time Blocks**: Define specific time periods for different types of appointments
2. **Block Types**: Categorize time blocks by appointment type (routine, urgent, procedures)
3. **Duration Settings**: Set standard appointment lengths for different visit types
4. **Buffer Time**: Configure time between appointments for documentation and transitions
5. **Break Periods**: Schedule lunch breaks and other non-clinical time

**Template Creation Process:**
1. Analyze provider workflow and patient population needs
2. Define block types and appointment durations
3. Create template structure with appropriate time allocations
4. Test template with sample scheduling scenarios
5. Refine based on provider feedback and utilization data

### Configure Block Types for Different Appointment Types

Block types organize provider time for specific purposes:

**Common Block Types:**
- **Routine Appointments**: Standard follow-up visits and preventive care
- **New Patient Appointments**: Initial consultations requiring longer time slots
- **Urgent Care**: Same-day sick visits and urgent concerns
- **Procedures**: Diagnostic tests, minor procedures, injections
- **Administrative Time**: Documentation, phone calls, care coordination
- **Teaching/Research**: Academic activities for providers in teaching hospitals

**Block Type Configuration:**
- Set default appointment durations for each block type
- Define patient population restrictions (new vs. established patients)
- Configure overbooking rules and limits
- Establish priority levels for different block types

### Set Up Recurring Schedule Patterns

Establish consistent weekly, monthly, or seasonal schedule patterns:

**Pattern Types:**
1. **Weekly Patterns**: Standard Monday-Friday clinic schedules
2. **Bi-weekly Patterns**: Alternating schedules for providers with multiple locations
3. **Monthly Patterns**: Complex rotations including hospital service, clinics, and procedures
4. **Seasonal Adjustments**: Modified schedules for holidays, academic calendars, or seasonal demands

**Implementation Considerations:**
- Account for provider preferences and work-life balance
- Consider patient access needs and demand patterns
- Plan for coverage during provider absences
- Integrate with call schedules and hospital duties

### Manage Provider Availability and Time Off

Coordinate scheduled absences and availability changes:

**Time Off Management:**
- Vacation scheduling and approval workflows
- Conference and continuing education time off
- Sick leave and unexpected absences
- Sabbatical and extended leave planning

**Coverage Arrangements:**
- Identify backup providers for scheduled absences
- Configure automatic schedule adjustments
- Set up patient notification for provider changes
- Manage appointment rescheduling processes

## Schedule Template Management

### Copy and Modify Existing Templates

Efficiently create new templates based on successful existing patterns:

**Template Copying Process:**
1. Identify successful template patterns from high-performing providers
2. Copy base template structure
3. Modify for specific provider needs and patient populations
4. Test new template in parallel with existing schedule
5. Implement changes with provider training and support

**Modification Considerations:**
- Adjust block types for different specialties
- Modify time allocations based on provider efficiency
- Customize for different patient populations
- Account for location-specific requirements

### Share Templates Across Providers

Standardize scheduling patterns across similar providers:

**Template Sharing Benefits:**
- Consistency in patient access across providers
- Simplified training for scheduling staff
- Easier schedule management and coverage arrangements
- Standardized metrics and performance comparisons

**Implementation Strategy:**
- Develop standard templates by specialty or department
- Allow customization for individual provider needs
- Establish governance process for template changes
- Monitor utilization and patient satisfaction across shared templates

### Version Control for Template Changes

Track and manage changes to provider schedule templates:

**Version Control Elements:**
- Document template change history and rationale
- Maintain backup copies of previous template versions
- Track performance metrics before and after changes
- Establish rollback procedures for unsuccessful changes

**Change Management Process:**
1. Analyze need for template modification
2. Design and test proposed changes
3. Implement changes with appropriate notice
4. Monitor impact on scheduling and provider satisfaction
5. Document lessons learned and best practices

## Advanced Scheduling Features

### Configure Double Booking Rules

Manage overbooking to optimize schedule utilization while maintaining quality:

**Double Booking Strategies:**
- Allow controlled overbooking for high no-show visit types
- Configure automatic waitlist management
- Set maximum overbooking limits by block type
- Implement provider-specific overbooking preferences

**Risk Management:**
- Monitor actual vs. scheduled appointment times
- Track patient wait times and satisfaction
- Adjust overbooking rules based on historical data
- Establish protocols for managing overbooked schedules

### Set Up Block Release Schedules

Automate the release of appointment blocks to optimize access:

**Release Schedule Configuration:**
- New patient blocks released at specified intervals
- Urgent care blocks held until day of service
- Specialty procedure blocks released with appropriate lead time
- Seasonal adjustments for demand patterns

**Benefits:**
- Improved access for different patient populations
- Better schedule utilization and reduced empty slots
- Automated management reducing manual scheduling work
- Flexible response to changing demand patterns

### Implement Schedule Optimization

Use data analytics to continuously improve scheduling effectiveness:

**Optimization Techniques:**
- Analyze historical scheduling patterns and patient flow
- Identify optimal appointment durations by visit type
- Adjust block allocations based on demand patterns
- Implement predictive scheduling based on patient characteristics

**Performance Monitoring:**
- Track schedule utilization rates by provider and block type
- Monitor patient access times and satisfaction scores
- Analyze no-show patterns and implement improvements
- Benchmark performance against organizational goals

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all provider schedule features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 8A9E2F3D-1B5C-4D7E-9F8A-3C6E9B2D4F7A