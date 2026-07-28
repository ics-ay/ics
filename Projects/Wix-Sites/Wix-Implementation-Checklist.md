# INTELEVATE Wix Implementation Checklist

## 1. Set Up Site Structure
1. Open Wix Editor for `intelevates.com`.
2. Create pages:
   - Home
   - About
   - Programs
   - Labs
   - For Corporates
   - For Institutions
   - Resources
   - Contact
3. Assign page URLs:
   - `/home`
   - `/about`
   - `/programs`
   - `/labs`
   - `/corporates`
   - `/institutions`
   - `/resources`
   - `/contact`
4. Configure the main site menu with the 8 pages.
5. Confirm page visibility and mobile menu order.

## 2. Build Page Sections

### Home
- Hero strip
  - Headline: “Intelligent learning for students, corporates, and institutions.”
  - Subheadline: “Career-ready programs, enterprise upskilling, and academic partnerships powered by AI.”
  - Buttons: `Choose Your Path`, `Book a Demo`, `Explore iLMS`
- Audience cards: Students, Corporates, Institutions
- Value bullets: outcome-driven, AI-enabled, Tier 2/3 India focus
- iLMS MVP preview section: highlight Local LLM prequalification and multi-tenant architecture
- Proof strip: partner logos, stats, testimonial teaser
- 3-step process strip: Discover → Prequalify → Start

### About
- Hero mission statement
- USP icon list:
  - Local AI-powered learning paths
  - Tier 2/3 India specialization
  - Secure enterprise-grade multi-tenancy
- Methodology section
- Trust section: partner logos, metrics, outcomes
- CTA: `Download Our Story`

### Programs
- Hero with program promise
- Program cards / tiles
- Benefits grid
- Outcome/testimonial card
- Enrollment process steps
- FAQ section

### Labs
- Hero: `iLMS MVP: AI prequalification, local LLM, and secure multi-tenancy`
- Feature cards:
  - Local LLM analysis
  - Digital prequalification
  - Curated learning paths
  - Partner integrations
- Use cases section: Students, Corporates, Institutions
- Demo CTA: `Request a Demo`

### For Corporates
- Hero with business value
- Solution cards: Reskilling, Manager Dashboards, Analytics
- ROI/outcome stats
- Trust logos/testimonial
- Engagement model section
- CTA: `Schedule Business Review`

### For Institutions
- Hero with academic partnership value
- Partnership models
- Benefits for students, faculty, institutions
- Technology support section
- CTA: `Request Academic Collaboration`

### Resources
- Hero with content hub message
- Category tiles: Student Success, Corporate Learning, Academic Innovation, Webinars
- Featured content block
- Newsletter signup
- Content list / filters

### Contact
- Hero with contact prompt
- Segmented lead form with audience selector
- Office/contact details
- Response-time note
- Footer CTA

## 3. Forms & CRM

### Forms to create
- Student Interest Form
- Corporate Partnership Form
- Institution Collaboration Form
- Newsletter Signup Form

### Field sets
- Common: Name, Email, Phone
- Student form: Program Interest, Preferred Start, Message
- Corporate form: Company, Role, Team Size, Training Need, Message
- Institution form: Institution Name, Role, Collaboration Type, Message
- Newsletter: Email, Interests checkbox

### CRM setup
- Create tags:
  - `student`
  - `corporate`
  - `institution`
  - `newsletter`
  - `webinar-attendee`
  - `demo-request`
  - `iLMS-interest`
- Create pipelines:
  - Student Enrollment
  - Corporate Sales
  - Institution Partnerships
  - Content Nurture
- Map each form submission to:
  - create/update contact
  - add audience tag
  - assign pipeline stage
  - record source page

## 4. Bookings & Events
1. Add Wix Bookings or Wix Events app.
2. Create event/services:
   - Student Info Session
   - Corporate Discovery Session
   - Academic Demo
3. Embed booking widgets on:
   - Home hero
   - Labs page
   - Contact page
   - Resources page
4. Tag registrants: `webinar-attendee`, `event-registrant`

## 5. Optional Members Area
1. Enable Members Area.
2. Create a private page: `Student Portal`.
3. Add gated sections: course access, onboarding resources, community updates.
4. Tag new members: `registered-student`
5. Send portal access onboarding email.

## 6. Blog / Resources Structure
1. Enable Wix Blog or Content Manager.
2. Create categories:
   - Student Success
   - Corporate Learning
   - Academic Innovation
   - Webinars
3. Create tags:
   - career-skills
   - L&D
   - education-technology
   - local-LLM
   - Tier-2/3
4. Add blog teasers to the Resources page.

## 7. Automations

### Student lead automation
- Trigger: Student Interest Form submit
- Actions:
  - send welcome email
  - tag `student`
  - add to Student Enrollment pipeline
  - notify admissions rep

### Corporate lead automation
- Trigger: Corporate Partnership Form submit
- Actions:
  - send acknowledgement email
  - tag `corporate`
  - add to Corporate Sales pipeline
  - create follow-up task

### Event automation
- Trigger: Booking registration
- Actions:
  - send confirmation email
  - tag `webinar-attendee`
  - send reminder 24 hours before event
  - send follow-up email after event

### Welcome / nurture automation
- Trigger: new contact or newsletter signup
- Actions:
  - send welcome sequence
  - add to nurture list
  - send targeted guide based on audience

## 8. SEO & Performance
1. Set page titles and meta descriptions for each page.
2. Ensure one clear H1 per page.
3. Add H2s for benefits, proof, and process.
4. Optimize all images in Wix; use alt text.
5. Limit heavy media and keep page sections focused.
6. Use internal links to connect Home, Programs, Labs, Corporates, Institutions, Resources, and Contact.

## 9. Launch Verification
1. Publish the site.
2. Test each form and confirm CRM contact creation.
3. Test booking registration flow and emails.
4. Verify SEO meta settings and page headings.
5. Review mobile layout in Wix Preview.
6. Confirm all CTAs and buttons are linked correctly.

## 10. Next Step
- Execute the above tasks sequentially in Wix Editor.
- Start with page creation and page structure.
- Then add forms/CRM, followed by bookings and automations.
- Finish with SEO settings and final verification.
