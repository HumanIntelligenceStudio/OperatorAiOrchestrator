# On My Way Setup and Support Guide

**Last Updated:** January 31, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 25687F6F-3200-409A-8E80-70B766ED4344

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Required On My Way Setup](#required-on-my-way-setup)
  - [Ensure That You Meet Prerequisites for On My Way](#ensure-that-you-meet-prerequisites-for-on-my-way)
  - [Configure Provider Records for On My Way](#configure-provider-records-for-on-my-way)
  - [Configure the Cadence Background User for On My Way](#configure-the-cadence-background-user-for-on-my-way)
  - [Determine General On My Way Behavior and Appearance in MyChart](#determine-general-on-my-way-behavior-and-appearance-in-mychart)
- [Cadence Based Departments](#cadence-based-departments)

## Overview

On My Way is a MyChart feature that allows patients to notify their healthcare providers when they are traveling to their appointment. This feature helps optimize clinic workflow by providing real-time updates on patient arrival status, enabling staff to better manage appointment schedules and reduce wait times.

## Required On My Way Setup

### Ensure That You Meet Prerequisites for On My Way

Before implementing On My Way, verify that your organization meets the following requirements:

**Technical Prerequisites:**
- MyChart must be implemented and active
- Mobile MyChart app must be available to patients
- Geolocation services must be enabled
- Push notification capability must be configured

**Organizational Prerequisites:**
- Appointment scheduling workflows must be established
- Check-in processes must be defined
- Staff training procedures must be in place
- Patient communication protocols must be established

### Configure Provider Records for On My Way

Provider records need specific configuration to support On My Way functionality:

1. **Enable On My Way for Providers**: Configure which providers will participate in On My Way notifications
2. **Set Notification Preferences**: Define how providers want to receive On My Way updates
3. **Configure Timing Parameters**: Set appropriate lead times for different appointment types
4. **Establish Override Settings**: Allow providers to customize On My Way behavior for specific situations

### Configure the Cadence Background User for On My Way

The Cadence background user processes On My Way notifications and updates:

1. **Create Background User Account**: Set up a dedicated system user for On My Way processing
2. **Assign Security Permissions**: Grant necessary access rights for appointment and notification management
3. **Configure Processing Parameters**: Set batch processing frequency and notification timing
4. **Test Background Processing**: Verify that automated processes work correctly

### Determine General On My Way Behavior and Appearance in MyChart

Configure how On My Way appears and functions for patients:

**User Interface Settings:**
- Button placement and appearance in MyChart
- Messaging text and language options
- Geolocation permission requests
- Notification timing and content

**Functional Behavior:**
- Distance thresholds for "on my way" notifications
- Automatic vs. manual notification options
- Integration with existing check-in processes
- Handling of traffic delays and estimated arrival times

## Cadence Based Departments

For departments using Cadence scheduling, additional configuration considerations include:

**Department-Specific Settings:**
- Customize On My Way behavior for different clinic types
- Set department-specific distance and timing thresholds
- Configure integration with department workqueues
- Establish department-specific notification preferences

**Workflow Integration:**
- Connect On My Way notifications with existing department workflows
- Configure automatic patient status updates
- Set up staff notification preferences
- Establish protocols for handling delayed or early arrivals

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all On My Way features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 25687F6F-3200-409A-8E80-70B766ED4344