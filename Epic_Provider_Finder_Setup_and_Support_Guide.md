# Provider Finder Setup and Support Guide

**Last Updated:** May 2, 2025

**Epic | 1979 Milky Way | Verona, WI 53593 | Voice: 608.271.9000 | Fax: 608.271.7237 | www.epic.com | documentation@epic.com**

**EpicUUID:** 31A5F01D-3957-459C-9FE7-FD29D8E5E7BD

## Your Responsibilities for Safe Use

This documentation will help guide you through the available software configuration options so you can decide the right configuration for your organization. Of course, safe and compliant use of the software in any configuration requires you and your users to use good judgment and perform certain responsibilities, including each of the following: enter and read information accurately and completely; be responsible for configuration decisions; ensure compliance with laws and regulations relevant for your organization; confirm the accuracy of critically important medical information (e.g., allergies, medications, results), just as you would with paper records; actively report suspected errors in the software to both Epic and affected personnel; thoroughly test the software to ensure it's accurate before using it; and use the software only according to standards of good medical practice. You also are responsible for training your personnel and other users to perform these responsibilities. Not performing any of these responsibilities may compromise patient safety or your compliance with applicable requirements.

## Table of Contents

- [How It Works](#how-it-works)
- [Available Epic Resources](#available-epic-resources)
- [Provider Finder Setup: Essentials](#provider-finder-setup-essentials)
  - [Control What Users See in Search Results](#control-what-users-see-in-search-results)
  - [Hide Unnecessary Provider Finder Filters](#hide-unnecessary-provider-finder-filters)
  - [Configure Provider Finder for Order Entry in EpicCare Ambulatory](#configure-provider-finder-for-order-entry-in-epiccare-ambulatory)

## Overview

Provider Finder helps users quickly locate and select appropriate providers within Epic applications. This tool streamlines provider selection processes across various workflows, from appointment scheduling to order entry, by providing robust search and filtering capabilities.

## How It Works

Provider Finder integrates throughout Epic to provide consistent provider search functionality:

**Core Functionality:**
- Real-time provider search with multiple filter options
- Integration with provider directory and scheduling information
- Customizable search results and display options
- Support for provider pools, subgroups, and individual providers
- Location-based and specialty-based filtering

**Search Capabilities:**
- Name-based searching with fuzzy matching
- Specialty and subspecialty filtering
- Location and department filtering
- Availability-based searching
- Custom attribute filtering

**Integration Points:**
- Appointment scheduling workflows
- Order entry and referral processes
- Provider directory maintenance
- Care team assignment
- Consultation requests

## Available Epic Resources

Epic provides several resources to support Provider Finder implementation:

- Foundation System configurations with example provider data
- Best practice guides for provider directory management
- Integration documentation for various Epic modules
- Training materials for end users and administrators
- Analytics tools for monitoring provider search patterns

## Provider Finder Setup: Essentials

### Control What Users See in Search Results

Configure search result display to show relevant information for your users:

**Result Display Configuration:**
1. **Provider Information Fields**: Select which provider details appear in search results
   - Provider name and credentials
   - Specialty and subspecialty information
   - Location and contact details
   - Schedule availability indicators
   - Patient panel status

2. **Result Sorting Options**: Configure default and available sorting methods
   - Alphabetical by provider name
   - Distance from patient location
   - Availability (soonest available appointment)
   - Specialty relevance
   - User-defined custom sorting

3. **Result Filtering**: Set up filters to help users narrow search results
   - Geographic filters (location, distance radius)
   - Specialty and subspecialty filters
   - Availability filters (accepting new patients, same-day availability)
   - Network and insurance participation filters
   - Language and cultural competency filters

### Hide Unnecessary Provider Finder Filters

Streamline the user interface by hiding filters that aren't relevant to your organization:

**Filter Management:**
1. **Assess Organizational Needs**: Determine which filters are relevant for your users
2. **Configure Visible Filters**: Show only the filters that add value to provider searches
3. **Set Default Filter Values**: Pre-populate commonly used filter settings
4. **Customize Filter Labels**: Use terminology that matches your organization's language

**Common Filter Categories:**
- Geographic filters (location, radius, zip code)
- Specialty and subspecialty filters
- Availability and scheduling filters
- Network participation and insurance filters
- Provider characteristics (gender, languages spoken)
- Patient population filters (pediatric, adult, geriatric)

### Configure Provider Finder for Order Entry in EpicCare Ambulatory

Optimize Provider Finder for clinical workflows in EpicCare Ambulatory:

**Order Entry Integration:**
1. **Referral Order Configuration**: Set up Provider Finder for consultation and referral orders
   - Specialty-specific provider lists
   - Preferred provider identification
   - Network and insurance validation
   - Automatic order routing based on provider selection

2. **Care Team Integration**: Configure Provider Finder for care team assignment
   - Primary care provider selection
   - Specialist assignment
   - Care coordinator assignment
   - Multi-disciplinary team configuration

3. **Clinical Decision Support**: Integrate Provider Finder with clinical guidelines
   - Specialty-appropriate provider suggestions
   - Quality metrics and outcome data integration
   - Provider performance indicators
   - Best practice recommendations

**Workflow Optimization:**
- Context-sensitive provider suggestions based on order type
- Integration with provider schedules and availability
- Automatic filtering based on patient location and insurance
- Quick access to recently used providers
- Favorites and preferred provider lists

*[Note: This is a condensed version of the full document. The complete guide contains detailed configuration steps, technical specifications, and implementation procedures for all Provider Finder features.]*

---

© 2018 - 2025 Epic Systems Corporation. All rights reserved. PROPRIETARY INFORMATION - This item and its contents may not be accessed, used, modified, reproduced, performed, displayed, distributed or disclosed unless and only to the extent expressly authorized by an agreement with Epic.

**EpicUUID:** 31A5F01D-3957-459C-9FE7-FD29D8E5E7BD