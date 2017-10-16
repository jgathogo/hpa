ra# User stories and activities
* As anyone I can visit apps.healthpovertyaction.or.ke and chose to see Call for Proposals
 * Project documentation
   * ~~Add a README file – explain what this project is all about~~
   * ~~Add this USERSTORIES.md~~
   * Update README - See [Github help pages](https://help.github.com/articles/about-readmes/) on how to write a helpful one.
   * Development [standards](https://lukeplant.me.uk/development-standards.html) by Luke Plant. Check these in order to 'close' this document:
        - Complete source code available
        - Dependencies documented
        - Dependencies kept up-to-date
        - Version Control System used for all sources
        - Automated tests for non-trivial functionality
        - Deployment scripts
        - Relevant standards and laws followed
        - Documentation included

 * Create landing home page with a list of HPA Apps
    * ~~Use Bootstrap to create website shell – include menus, header and footers~~
    * ~~Bootstrap – CDN or host locally? Consider pros and cons~~
    * ~~Create static folder for CSS, JS etc~~
    * Make sidebar items toggleable
*****
* As anyone, I can view calls for proposals by country, closing date for applications, theme, donor
* As a Programme Manager of Country X, I can view the calls for proposals specific to my country
* As a Programme Manager of Country X, I can view the calls for proposals specific to my country by theme
* As a Programme Manager of Country X, I can view the calls for proposals specific to my country by theme
* As a Programme Manager of Country X, I can view the calls for proposals specific to my country by closing date for applications
* As Staff, I can view calls for proposals
* As Staff, I can view calls for proposals by Theme
* As Staff, I can view calls for proposals by closing date for applications
    * ~~Better URL presentation to include a slug perhaps e.g., cfp/donor-cfp-title~~
    * Make the website RESTful
    * Present call for proposals by deadline date, in the following categories, if they exist – 1) current month, 2) each of the next 5 months 3) ongoing (with no deadline)
    * User can chose/search by country, theme, donor – dynamic menus for this? Or do we let user choose from drop-down list?
    * Users can download page – PDF, spreadsheet, email, share online etc.
*****
* As an Authorised User, I can add a donor, CfP, theme and zone
* As an Authorised User, I can edit a donor, CfP, theme and zone
* As a Super User, I can add, edit and/or delete a donor, CfP, theme and zone
    * User authentication. Start with normal Django users followed by Gmail.
    * Create data entry form – paragraph fields should include formatting (e.g., tinymce)
    * Data entry form should be able dynamic – hide fields/prompt user based on input, perform necessary validation
    * Mandatory fields will need to be filled
    * If for example, the User choses that a CfP has a deadline date, they should be taken to the date field. If not, date field should be disabled.
*****
* As a Programme Manager for Country X, I want to receive notification about new upcoming calls for proposals specific to my country
* As the Head of Programmes - Africa, I want to receive notification about new upcoming calls for proposals for countries in Africa
* As a Super User, I want to receive notification of any change to the donor, CfP, theme and zone
* When CfP is updated – any update – let SuperUser know
* If a new CfP is added notify, Head of Programmes and specific Programme Manager. New add should first check if the Programme Manager for a particular country is in the database and prompt user to fill in their details.
