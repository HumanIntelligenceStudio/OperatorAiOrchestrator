# Visit Types Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 5A7D2F8B-9E1C-4A6F-8D3B-7F2E9A5C1D8F

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Visit Type Fundamentals](#visit-type-fundamentals)
  - [Understanding Visit Types in Epic](#understanding-visit-types-in-epic)
  - [Visit Type Categories and Classifications](#visit-type-categories-and-classifications)
  - [Planning Your Visit Type Strategy](#planning-your-visit-type-strategy)
- [Visit Type Configuration](#visit-type-configuration)
  - [Create Basic Visit Type Records](#create-basic-visit-type-records)
  - [Configure Visit Type Attributes](#configure-visit-type-attributes)
  - [Set Up Duration and Scheduling Parameters](#set-up-duration-and-scheduling-parameters)
  - [Configure Patient Population Restrictions](#configure-patient-population-restrictions)
- [Advanced Visit Type Features](#advanced-visit-type-features)
  - [Set Up Visit Type Groups and Families](#set-up-visit-type-groups-and-families)
  - [Configure Multi-Resource Visit Types](#configure-multi-resource-visit-types)
  - [Implement Dynamic Visit Type Selection](#implement-dynamic-visit-type-selection)
- [Integration and Workflow](#integration-and-workflow)
  - [Integrate Visit Types with Clinical Documentation](#integrate-visit-types-with-clinical-documentation)
  - [Configure Billing and Charge Capture](#configure-billing-and-charge-capture)
  - [Set Up Quality Metrics and Reporting](#set-up-quality-metrics-and-reporting)

## Overview

Visit types are fundamental building blocks of Epic's scheduling system that define the nature, duration, and requirements of patient appointments. Proper visit type configuration is essential for efficient scheduling, accurate billing, appropriate resource allocation, and meaningful clinical documentation and reporting.

## Visit Type Fundamentals

### Understanding Visit Types in Epic

Visit types serve multiple purposes within Epic's integrated system:

**Primary Functions:**
1. **Scheduling Foundation**: Define appointment types available for booking
2. **Duration Management**: Establish standard appointment lengths
3. **Resource Allocation**: Specify required providers, rooms, and equipment
4. **Billing Integration**: Link appointments to appropriate charge structures
5. **Clinical Workflow**: Guide documentation and care delivery processes

**System Integration:**
- Appointment scheduling and calendar management
- Clinical documentation templates and workflows
- Billing and charge capture processes
- Quality reporting and outcome tracking
- Patient portal and self-scheduling functionality

### Visit Type Categories and Classifications

Organize visit types into logical categories for effective management:

**Common Visit Type Categories:**
1. **New Patient Visits**: Initial consultations and comprehensive evaluations
2. **Follow-Up Visits**: Routine monitoring and ongoing care management
3. **Preventive Care**: Health maintenance and screening appointments
4. **Acute Care**: Urgent and same-day sick visits
5. **Procedures**: Diagnostic tests, minor surgeries, and interventions
6. **Consultations**: Specialist evaluations and second opinions

**Specialty-Specific Categories:**
- Primary Care: Annual physicals, chronic disease management, acute illness
- Cardiology: Echo studies, stress tests, follow-up consultations
- Orthopedics: New injury evaluations, post-operative follow-ups, injections
- Pediatrics: Well-child visits, immunizations, developmental assessments
- Surgery: Pre-operative consultations, post-operative follow-ups

### Planning Your Visit Type Strategy

Develop a comprehensive strategy for visit type implementation:

**Strategic Considerations:**
1. **Clinical Workflow Alignment**: Match visit types to actual care delivery patterns
2. **Provider Preferences**: Accommodate individual provider scheduling preferences
3. **Patient Population Needs**: Reflect the specific needs of patient demographics
4. **Resource Optimization**: Balance efficiency with quality of care
5. **Quality Measurement**: Support quality reporting and improvement initiatives

**Implementation Approach:**
- Start with high-volume, standardized visit types
- Gradually add complexity and specialty-specific types
- Continuously refine based on utilization data and feedback
- Maintain consistency across similar departments and providers
- Plan for future growth and service line expansion

## Visit Type Configuration

### Create Basic Visit Type Records

Establish fundamental visit type records with essential information:

**Required Configuration Elements:**
1. **Visit Type Name**: Clear, descriptive names for easy identification
2. **Visit Type Abbreviation**: Short codes for scheduling displays
3. **Department Assignment**: Link to specific departments and service lines
4. **Provider Types**: Specify which providers can deliver this visit type
5. **Active Status**: Control availability for scheduling

**Basic Setup Process:**
1. Define visit type naming conventions and standards
2. Create master list of required visit types by department
3. Configure basic visit type records with essential attributes
4. Test visit type functionality in scheduling systems
5. Activate visit types for live scheduling use

### Configure Visit Type Attributes

Set detailed attributes that control visit type behavior:

**Key Attributes:**
1. **Visit Duration**: Standard appointment length in minutes
2. **Buffer Time**: Pre and post-appointment time for preparation
3. **Patient Class**: Link to appropriate billing and insurance categories
4. **Location Requirements**: Specify required rooms or locations  
5. **Equipment Needs**: Define necessary medical equipment or resources

**Scheduling Attributes:**
- Lead time requirements (minimum advance booking)
- Maximum future booking limits
- Weekend and holiday availability
- Time-of-day restrictions
- Seasonal availability patterns

### Set Up Duration and Scheduling Parameters

Configure timing and scheduling rules for each visit type:

**Duration Configuration:**
1. **Standard Duration**: Typical appointment length
2. **Minimum Duration**: Shortest acceptable appointment time
3. **Maximum Duration**: Longest allowable appointment time
4. **Variable Duration**: Allow scheduling flexibility for complex cases
5. **Buffer Time**: Pre/post appointment time for transitions

**Scheduling Parameters:**
- Double-booking rules and overbooking limits
- Block release schedules for different patient populations
- Priority settings for urgent vs. routine appointments
- Integration with wait list and Fast Pass functionality
- Automatic reminder and confirmation settings

### Configure Patient Population Restrictions

Define which patients can be scheduled for specific visit types:

**Restriction Types:**
1. **Age Restrictions**: Pediatric vs. adult vs. geriatric populations
2. **Patient Status**: New patient vs. established patient requirements
3. **Insurance Requirements**: Payer-specific visit type restrictions
4. **Clinical Conditions**: Diagnosis or condition-specific limitations
5. **Geographic Restrictions**: Location-based scheduling rules

**Implementation Considerations:**
- Balance access with appropriateness of care
- Consider clinical safety and competency requirements
- Accommodate emergency and urgent care exceptions
- Integrate with provider credentialing and privileges
- Support quality improvement and outcome measurement

## Advanced Visit Type Features

### Set Up Visit Type Groups and Families

Organize related visit types for efficient management:

**Visit Type Groups:**
1. **Functional Groups**: Related visit types serving similar purposes
2. **Provider Groups**: Visit types specific to provider types or specialties
3. **Billing Groups**: Visit types with similar billing characteristics
4. **Quality Groups**: Visit types tracked for quality measures
5. **Reporting Groups**: Visit types for analytics and performance reporting

**Family Relationships:**
- Parent-child relationships for visit type hierarchies
- Shared attributes and inheritance rules
- Bulk configuration changes and updates
- Consistent reporting and analytics
- Simplified maintenance and management

### Configure Multi-Resource Visit Types

Set up visit types requiring multiple providers or resources:

**Multi-Resource Requirements:**
1. **Multiple Providers**: Team-based care delivery models
2. **Specialized Equipment**: Complex procedures requiring specific resources
3. **Room Requirements**: Specialized facilities or environments
4. **Support Staff**: Nursing, technical, or administrative support
5. **Time Coordination**: Synchronized scheduling of multiple resources

**Configuration Complexity:**
- Resource availability checking and coordination
- Scheduling optimization for multiple constraints
- Cancellation and rescheduling impact management
- Cost allocation and billing complexity
- Quality measurement for team-based care

### Implement Dynamic Visit Type Selection

Enable intelligent visit type selection based on patient characteristics:

**Dynamic Selection Criteria:**
1. **Clinical Indicators**: Diagnosis, symptoms, or chief complaint
2. **Patient History**: Previous visits, procedures, or conditions
3. **Provider Relationships**: Established care relationships
4. **Insurance Coverage**: Payer requirements and authorizations
5. **Geographic Factors**: Location, distance, or accessibility needs

**Implementation Benefits:**
- Improved scheduling accuracy and appropriateness
- Reduced scheduling errors and patient confusion
- Enhanced patient experience through personalized service
- Better resource utilization and efficiency
- Support for evidence-based scheduling practices

## Integration and Workflow

### Integrate Visit Types with Clinical Documentation

Link visit types to appropriate clinical documentation workflows:

**Documentation Integration:**
1. **Note Templates**: Visit type-specific documentation templates
2. **Order Sets**: Standardized orders for specific visit types
3. **Clinical Pathways**: Evidence-based care protocols
4. **Quality Measures**: Automated quality metric tracking
5. **Coding Support**: ICD-10 and CPT code suggestions

**Workflow Benefits:**
- Standardized clinical documentation practices
- Improved coding accuracy and compliance
- Enhanced quality measurement and reporting
- Reduced provider documentation burden
- Better clinical decision support integration

### Configure Billing and Charge Capture

Ensure accurate billing through proper visit type configuration:

**Billing Configuration:**
1. **Charge Schedules**: Link visit types to appropriate charges
2. **Insurance Rules**: Payer-specific billing requirements
3. **Modifier Requirements**: Procedure and diagnostic modifiers
4. **Bundle Rules**: Package pricing and service bundling
5. **Authorization Requirements**: Prior approval and referral needs

**Revenue Optimization:**
- Accurate charge capture and billing
- Reduced claim denials and rejections
- Improved compliance with billing regulations
- Enhanced revenue cycle management
- Better financial reporting and analysis

### Set Up Quality Metrics and Reporting

Configure visit types to support quality improvement initiatives:

**Quality Integration:**
1. **Performance Measures**: Clinical quality indicators
2. **Patient Satisfaction**: Experience measurement and tracking
3. **Outcome Tracking**: Clinical outcomes and effectiveness
4. **Efficiency Metrics**: Productivity and utilization measures
5. **Comparative Analytics**: Benchmarking and best practice identification

**Reporting Capabilities:**
- Automated quality reporting and dashboards
- Provider performance measurement and feedback
- Population health management and analytics
- Continuous improvement identification and implementation
- Regulatory reporting and compliance monitoring

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all visit type features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 5A7D2F8B-9E1C-4A6F-8D3B-7F2E9A5C1D8F