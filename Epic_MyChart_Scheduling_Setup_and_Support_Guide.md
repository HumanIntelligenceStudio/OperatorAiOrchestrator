# MyChart Scheduling Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** B0762ADD-6C22-4227-B345-76F0B4E1D3C5

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Available Epic Resources](#available-epic-resources)
- [MyChart Scheduling Strategy](#mychart-scheduling-strategy)
  - [Why Allow Patients to Schedule Through MyChart?](#why-allow-patients-to-schedule-through-mychart)
  - [Ticket Scheduling Recommendations](#ticket-scheduling-recommendations)
  - [Open Scheduling Recommendations](#open-scheduling-recommendations)
  - [Direct Scheduling Recommendations](#direct-scheduling-recommendations)

## Overview

MyChart scheduling empowers patients to schedule their own appointments online, improving patient satisfaction while reducing administrative workload for your staff. Epic provides multiple scheduling methods through MyChart to meet different organizational needs and patient preferences.

## Available Epic Resources

Epic provides several resources to support MyChart scheduling implementation:

- Foundation System configurations and examples
- Best practice guides for patient self-scheduling
- User training materials and patient education resources
- Integration guides for third-party systems
- Analytics and reporting tools for monitoring scheduling patterns

## MyChart Scheduling Strategy

### Why Allow Patients to Schedule Through MyChart?

Patient self-scheduling through MyChart offers numerous benefits:

**For Patients:**
- 24/7 access to schedule appointments
- Immediate confirmation of appointment availability
- Ability to see all available appointment times
- Reduced wait times on hold with scheduling staff
- Greater control over their healthcare scheduling

**For Organizations:**
- Reduced phone call volume to scheduling departments
- Improved staff efficiency and productivity
- Better schedule utilization and reduced no-shows
- Enhanced patient satisfaction scores
- Decreased labor costs for routine scheduling tasks

**For Providers:**
- Fuller schedules with better utilization
- Reduced last-minute cancellations
- More engaged patients who actively participate in scheduling

### Ticket Scheduling Recommendations

Ticket scheduling allows patients to request appointments that are then reviewed and scheduled by your staff.

**Best Use Cases:**
- New patient appointments requiring screening
- Complex procedures requiring pre-authorization
- Appointments requiring specific preparation or coordination
- Visits with limited provider availability

**Configuration Recommendations:**
- Set up clear instructions for patients about what information to provide
- Configure automatic routing to appropriate scheduling staff
- Establish response time expectations for ticket processing
- Use decision trees to gather necessary pre-visit information

### Open Scheduling Recommendations

Open scheduling allows patients to directly book into available appointment slots without staff intervention.

**Best Use Cases:**
- Routine follow-up appointments
- Well-established patients with providers
- Visit types that don't require special preparation
- High-volume, standardized appointment types

**Configuration Recommendations:**
- Carefully control which appointment types are available for open scheduling
- Set appropriate lead time restrictions (e.g., minimum 24-48 hours in advance)
- Configure automatic confirmation and reminder systems
- Monitor and adjust availability to maintain optimal schedule utilization

### Direct Scheduling Recommendations

Direct scheduling provides immediate appointment booking with instant confirmation.

**Best Use Cases:**
- Established patients with their regular providers
- Routine visits (annual checkups, medication follow-ups)
- Non-urgent specialty consultations
- Appointments that can be standardized

**Configuration Recommendations:**
- Implement robust decision trees to ensure appropriate visit type selection
- Set up automated patient preparation instructions
- Configure insurance verification workflows
- Establish clear cancellation and rescheduling policies

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all MyChart scheduling features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** B0762ADD-6C22-4227-B345-76F0B4E1D3C5