# Fast Pass Setup and Support Guide

**Last Updated:** November 1, 2024

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 6DB0D57A-C621-4B03-890C-913C404323C3

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [Fast Pass Strategy](#fast-pass-strategy)
  - [Why Use Fast Pass?](#why-use-fast-pass)
  - [Analysis and Build](#analysis-and-build)
- [Fast Pass Setup: Essentials](#fast-pass-setup-essentials)
  - [Identify and Send Fast Pass Offers from the Wait List](#identify-and-send-fast-pass-offers-from-the-wait-list)
  - [Notify Patients When There Is a Wait List Offer](#notify-patients-when-there-is-a-wait-list-offer)
  - [Allow Cadence Users to See, Schedule, and Overrule Fast Pass Offers](#allow-cadence-users-to-see-schedule-and-overrule-fast-pass-offers)
  - [Let Patients Update Wait List Status from MyChart](#let-patients-update-wait-list-status-from-mychart)
  - [Notify Patients When an Unscheduled Ticket Has Availability](#notify-patients-when-an-unscheduled-ticket-has-availability)
  - [Enable Fast Pass for Open Scheduling](#enable-fast-pass-for-open-scheduling)
- [Fast Pass Setup: Bells and Whistles](#fast-pass-setup-bells-and-whistles)
  - [Send Offers to Patients Based on Risk Scores](#send-offers-to-patients-based-on-risk-scores)
  - [Track a Patient's Reason for Joining the Wait List](#track-a-patients-reason-for-joining-the-wait-list)
- [Fast Pass Support: Ongoing Tasks](#fast-pass-support-ongoing-tasks)
  - [Monitor Fast Pass Effectiveness](#monitor-fast-pass-effectiveness)
- [Fast Pass Support: Troubleshooting and Common Issues](#fast-pass-support-troubleshooting-and-common-issues)
  - [Troubleshooting](#troubleshooting)
  - [No offers are being sent to patients](#no-offers-are-being-sent-to-patients)
  - [Some wait list entries are not being considered for offers](#some-wait-list-entries-are-not-being-considered-for-offers)

## Overview

Fast Pass is a wait list feature in Cadence that automatically sends patients text or email messages to notify them of a wait list appointment offering. Upon receiving the message, patients can then log in to the MyChart website or MyChart mobile app and claim the offer if it is still available or decline the offer to keep the original appointment and wait for another offer.

Fast Pass increases schedule utilization and patient satisfaction because providers' schedules are fuller and patients have the opportunity to be seen by providers earlier than originally scheduled. Fast Pass also relieves front desk staff from calling patients on the wait list to fill openings in the schedule.

For information about how Johns Hopkins Medicine implemented Fast Pass, refer to the Keep Provider Schedules Full and Reduce Front Desk Workload with Fast Pass document.

## How It Works

Here's a visual overview of how the system uses a wait list report to find available openings and send offers to a single patient, and what happens when a patient accepts or declines an offer:

*[Visual diagram would be here in the original document]*

And here's a visual overview of sending offers to multiple patients at once:

*[Visual diagram would be here in the original document]*

1. You set up one or more batch jobs to periodically search through wait list entries and look for potential appointments for those entries. In these batch jobs, you control which wait list reports to search, the priority of wait list entries, and whether to offer possible openings to multiple patients or one patient at a time, as well as other search behavior.

2. If a batch job finds an appointment time that matches a wait list entry, the patient is MyChart active, and the patient has opted in for these types of notifications, the system sends the patient a text message or email. If the patient isn't signed up to receive text messages or emails, the system won't send them offers.

3. The patient uses the information in the text message or email to go to their MyChart account. From here, the patient can take one of several actions.
   - If the patient accepts the offer, the system cancels any previous appointments and schedules the new appointment based on the wait list entry. If you send offers to multiple patients at once, other patients offered the appointment see that the offer is no longer available.
   - If the patient declines the offer and keeps their original appointment, the system offers the time to the next applicable patient the next time the batch runs if you send offers to one patient at a time. If you send offers to multiple patients, the offer stands until it expires or until a patient accepts the offer.
   - If the patient doesn't accept or decline the offer in a specific amount of time that you define, the offer expires for that patient. If you send the offer to multiple patients at the same time, each patient has the same time frame in which to take action on the offer. If you sent the offer to one patient at a time, the system offers the time to the next applicable patient the next time the batch runs.
   - If the patient calls the clinic regarding the offer, schedulers can accept or decline the offer for the patient using actions from the Appointment Desk.

## Fast Pass Strategy

This section includes important considerations to take into account as you plan to implement Fast Pass in MyChart. Additional strategy information is available for specific types of scheduling, although many of the concepts below still apply. Refer to the following resources for more information:

- MyChart Scheduling Setup and Support Guide
- Open Scheduling Setup and Support Guide
- Wait List Setup and Support Guide

### Why Use Fast Pass?

Fast Pass automatically sends notifications to MyChart patients about possible appointment openings. The ability for patients to accept earlier appointment slots will help keep providers' schedules full at your organization. Additionally, Fast Pass can increase patient satisfaction by offering earlier openings without having to contact the clinic.

### Analysis and Build

This section contains a number of Epic recommendations for how to most effectively implement Fast Pass at your organization. We also recommend reviewing the build considerations in Johns Hopkins financial program, Keep Provider Schedules Full and Reduce Front Desk Workload with Fast Pass, to model your build.

The Cadence team should take the lead on this project, but they'll need to work with the MyChart team for testing and to configure the MyChart pieces, including security, notifications, and the tickler messages.

The time required to complete analysis of this feature will vary depending on coordination between your IT and operations teams to decide on build settings and a pilot program. After analysis, build requires a few hours to a day to complete. The primary decisions are to determine which wait lists to use, whether to send offers to multiple patients at a time, and whether to allow patients to add themselves to the wait list. Although Fast Pass can be beneficial for most areas if patients are allowed to add themselves to the wait list, departments that might be a good fit for Fast Pass are those that:

- Use the wait list today.
- Have a meaningful percentage of their patient population using MyChart.
- Have room for improvement in utilization, or struggle with late cancellations or lead time.

Cadence analysts need to make security changes, set up a batch job, and configure the Appointment Desk so schedulers can accept and decline offers. MyChart analysts need to add the tickler and alert types to the MyChart settings.

There is minimal training needed for Fast Pass because the system does most of the work. You should let schedulers and front desk users know about this new feature so that they can answer patient questions and so they can schedule the wait list offers if a patient calls to schedule rather than using MyChart. You might also remind these users to collect mobile phone numbers and emails from patients, so that patients can receive offers.

After implementing Fast Pass, notify patients so that they can sign up to use MyChart and receive appointment offers. And let your MyChart help desk staff know that you've implemented this feature so they can assist patients with any questions.

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all Fast Pass features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 6DB0D57A-C621-4B03-890C-913C404323C3