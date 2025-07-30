# Provider/Resource (SER) Master File Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 2F8B4E1A-9C3D-4B7E-8F1A-5D6C2E9B3F8A

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Provider Master File Basics](#provider-master-file-basics)
  - [Create Provider Records](#create-provider-records)
  - [Configure Provider Demographics and Credentials](#configure-provider-demographics-and-credentials)
  - [Set Up Provider Specialties and Subspecialties](#set-up-provider-specialties-and-subspecialties)
  - [Manage Provider Licensing and Certification Information](#manage-provider-licensing-and-certification-information)
- [Resource Configuration](#resource-configuration)
  - [Create Resource Records for Non-Provider Scheduling](#create-resource-records-for-non-provider-scheduling)
  - [Configure Equipment and Room Resources](#configure-equipment-and-room-resources)
  - [Set Up Shared Resources and Resource Pools](#set-up-shared-resources-and-resource-pools)
- [Provider-Department Relationships](#provider-department-relationships)
  - [Link Providers to Departments](#link-providers-to-departments)
  - [Configure Provider Templates by Department](#configure-provider-templates-by-department)
  - [Manage Provider Privileges and Restrictions](#manage-provider-privileges-and-restrictions)
- [Advanced Provider Configuration](#advanced-provider-configuration)
  - [Set Up Provider Groups and Teams](#set-up-provider-groups-and-teams)
  - [Configure Provider Hierarchies](#configure-provider-hierarchies)
  - [Implement Provider Coverage Relationships](#implement-provider-coverage-relationships)

## Overview

The Provider/Resource (SER) Master File serves as the central repository for all provider and resource information in Epic. This includes clinical providers, support staff, equipment, rooms, and other schedulable resources. Proper setup and maintenance of the SER master file is crucial for effective scheduling, billing, reporting, and clinical workflow management.

## Provider Master File Basics

### Create Provider Records

Provider records form the foundation of Epic's provider management system:

**Essential Provider Information:**
1. **Basic Demographics**: Name, credentials, contact information
2. **Professional Identifiers**: NPI numbers, state license numbers, DEA numbers
3. **Employment Information**: Employment status, hire date, department affiliations
4. **Clinical Information**: Specialties, subspecialties, areas of expertise
5. **Scheduling Information**: Schedule templates, availability patterns

**Provider Record Creation Process:**
1. Gather all required provider information and documentation
2. Create basic provider record with demographics and identifiers
3. Configure specialty and subspecialty information
4. Set up department relationships and scheduling parameters
5. Test provider record functionality across Epic modules
6. Activate provider record for live use

### Configure Provider Demographics and Credentials

Accurate demographic and credential information supports clinical operations and compliance:

**Demographic Configuration:**
- Full legal name and preferred display name
- Professional credentials and degree information
- Contact information (phone, email, pager)
- Photo upload for provider identification
- Preferred communication methods

**Credential Management:**
- Medical degree and training information
- Board certifications and recertification dates
- Professional memberships and affiliations
- Continuing education tracking
- Quality metrics and performance indicators

### Set Up Provider Specialties and Subspecialties

Specialty configuration enables proper provider matching and referral routing:

**Specialty Setup Components:**
1. **Primary Specialty**: Main area of clinical practice
2. **Subspecialties**: Additional areas of expertise
3. **Procedure Specialties**: Specific procedures and interventions
4. **Research Interests**: Academic and research focus areas
5. **Patient Population Focus**: Age groups, conditions, demographics

**Clinical Applications:**
- Provider directory and search functionality
- Referral routing and provider matching
- Scheduling optimization and patient placement
- Quality reporting and outcome tracking
- Network adequacy and coverage analysis

### Manage Provider Licensing and Certification Information

Track and maintain provider licensing and certification status:

**Licensing Information:**
- State medical licenses with expiration dates
- DEA registrations and controlled substance authority
- Hospital privileges and credentialing status
- Specialty board certifications
- Professional liability insurance information

**Compliance Monitoring:**
- Automated alerts for expiring licenses and certifications
- Integration with credentialing workflow systems
- Documentation of continuing education requirements
- Tracking of quality assurance activities
- Maintenance of professional references and background checks

## Resource Configuration

### Create Resource Records for Non-Provider Scheduling

Resource records enable scheduling of equipment, rooms, and services:

**Types of Resources:**
1. **Equipment Resources**: Medical devices, diagnostic equipment, surgical instruments
2. **Room Resources**: Exam rooms, procedure rooms, operating theaters
3. **Service Resources**: Interpreters, transportation, support services
4. **Virtual Resources**: Telemedicine platforms, remote monitoring systems

**Resource Configuration Elements:**
- Resource name, description, and category
- Availability schedule and booking rules
- Capacity limitations and usage restrictions
- Maintenance schedules and downtime periods
- Cost centers and billing information

### Configure Equipment and Room Resources

Specialized configuration for physical resources:

**Equipment Resource Setup:**
- Equipment specifications and capabilities
- Maintenance schedules and service requirements
- Safety protocols and usage guidelines
- Quality control and calibration tracking
- Integration with asset management systems

**Room Resource Configuration:**
- Room capacity and physical characteristics
- Equipment available in each room
- Accessibility features and special accommodations
- Environmental controls and safety systems
- Scheduling priority and usage rules

### Set Up Shared Resources and Resource Pools

Manage resources shared across multiple departments or providers:

**Shared Resource Management:**
- Define sharing rules and priorities
- Configure booking restrictions and approval processes
- Set up cost allocation and billing procedures
- Establish maintenance and responsibility protocols
- Monitor utilization and optimize allocation

**Resource Pool Configuration:**
- Group similar resources for flexible scheduling
- Define pool availability and booking rules
- Configure automatic resource assignment
- Set up backup and contingency resources
- Monitor pool utilization and performance

## Provider-Department Relationships

### Link Providers to Departments

Establish provider affiliations with departments and service lines:

**Department Relationship Types:**
1. **Primary Department**: Main departmental affiliation
2. **Secondary Departments**: Additional affiliations and cross-coverage
3. **Service Line Participation**: Multidisciplinary team membership
4. **Administrative Relationships**: Committee participation, leadership roles

**Configuration Considerations:**
- Scheduling template assignment by department
- Billing and charge capture rules
- Security and access permissions
- Reporting relationships and metrics
- Quality improvement initiatives

### Configure Provider Templates by Department

Customize provider schedules for different departmental needs:

**Template Customization:**
- Department-specific block types and visit categories
- Patient population focus by department
- Procedure and service offerings
- Coverage requirements and call schedules
- Performance metrics and productivity targets

**Multi-Department Providers:**
- Coordinate schedules across multiple departments
- Manage conflicting priorities and commitments
- Optimize resource utilization and patient access
- Maintain consistency in care delivery
- Support provider work-life balance

### Manage Provider Privileges and Restrictions

Configure clinical privileges and practice limitations:

**Privilege Categories:**
- Admitting privileges and hospital access
- Procedure authorizations and limitations
- Prescribing authority and controlled substances
- Clinical decision-making scope
- Teaching and supervision responsibilities

**Restriction Management:**
- Temporary practice limitations
- Peer review and quality improvement actions
- Continuing education requirements
- Scope of practice modifications
- Compliance with organizational policies

## Advanced Provider Configuration

### Set Up Provider Groups and Teams

Organize providers into functional groups for scheduling and workflow:

**Group Types:**
1. **Call Groups**: Shared call responsibilities
2. **Coverage Groups**: Backup and substitute arrangements
3. **Care Teams**: Multidisciplinary patient care coordination
4. **Quality Groups**: Peer review and improvement activities
5. **Administrative Groups**: Committee and governance participation

**Team Configuration:**
- Define team membership and roles
- Configure communication preferences
- Set up workflow and task distribution
- Establish performance metrics and goals
- Monitor team effectiveness and outcomes

### Configure Provider Hierarchies

Establish reporting relationships and supervisory structures:

**Hierarchy Components:**
- Attending and resident physician relationships
- Supervisory responsibilities and oversight
- Teaching and mentoring assignments
- Quality assurance and peer review
- Administrative reporting structures

**Clinical Applications:**
- Cosigning requirements for orders and documentation
- Consultation and referral routing
- Quality improvement and patient safety
- Education and competency assessment
- Compliance monitoring and documentation

### Implement Provider Coverage Relationships

Configure provider backup and coverage arrangements:

**Coverage Types:**
- Vacation and conference coverage
- Sick leave and emergency coverage
- Call schedule backup arrangements
- Specialty consultation coverage
- Administrative duty coverage

**Configuration Elements:**
- Define coverage relationships and preferences
- Set up automatic notification systems
- Configure patient communication for provider changes
- Establish quality and continuity standards
- Monitor coverage effectiveness and patient satisfaction

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all SER master file features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 2F8B4E1A-9C3D-4B7E-8F1A-5D6C2E9B3F8A