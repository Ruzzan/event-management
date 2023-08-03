JAZZMIN_SETTINGS = {
    "site_title": "Evemo Superadmin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Evemo Superadmin",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Evemo Superadmin",

    # Logo to use for your site, must be present in static files, used for brand on top left
    # "site_logo": "books/img/logo.png",

    # Logo to use for your site, must be present in static files, used for login form logo (defaults to site_logo)
    "login_logo": None,

    # Logo to use for login form in dark themes (defaults to login_logo)
    "login_logo_dark": None,

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": None,

    # Welcome text on the login screen
    "welcome_sign": "Evemo Admin",

    # Copyright on the footer
    "copyright": "Evemo",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": None,

    # Field name on user model that contains avatar image
    "user_avatar": "fas fa-user",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index",},
        {"app": "events"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        {"model": "users.User"}
    ],

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        # apps
        "events",
        "users",
        "core",

        # models
        # "core.Interest",
        "core.Contact",

        "events.Event",
        "events.Application",

        "users.User",
    ],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
    },

    # model icons
    "icons": {
        "users.User": "fas fa-user",
        
        "core.Sector":"fas fa-clipboard-list",
        "core.Skill":"fas fa-laptop-code",

        "core.Faq":"fas fa-question",
        "core.Metric":"fas fa-chart-bar",
        "core.Quote":"fas fa-quote-left",
        "core.Testimonial":"fas fa-comment-dots",
        
        "community.Community":"fas fa-home",
        "community.Accomodation":"fas fa-bed",
        "community.Attraction":"fas fa-star",
        "community.CommuneGallery":"fas fa-image",

        "events.Event":"fas fa-calendar-alt",
        "events.EventApplication":"fas fa-file",
        "events.EventInquiry":"fas fa-comment",
        "events.Facilitator":"fas fa-user",
        "events.EventCategory":"fas fa-list",
        "events.EventParticipant":"fas fa-users",
        "events.EventSchedule":"fas fa-clock",

        "blogs.Post":"fas fa-newspaper",
        "blogs.Category":"fas fa-list",

        "users.OTP":"fas fa-lock",

        "about.About":"fas fa-globe",
        
        "contacts.Contact":"fas fa-comment",
        "contacts.Newsletter":"fas fa-paper-plane",

        "roles.Role":"fas fa-address-card",

        "resources.Audio":"fas fa-headphones",
        "resources.Video":"fas fa-video",
        "resources.Gallery":"fas fa-folder",
        "resources.GalleryImage":"fas fa-image",

        "notifications.Notification":"fas fa-bell",
        "notifications.GlobalNotification":"fas fa-bullhorn",
        "notifications.PushNotification":"fas fa-bell",

        "members.Member":"fas fa-user-tag",

        "sites.Site":"fas fa-server",
        "account.EmailAddress":"fas fa-at",
        "authtoken.TokenProxy":"fas fa-key",
        "background_task.task":"fas fa-sitemap",
        "background_task.completedtask":"fas fa-folder-open",
        "django_summernote.Attachment":"fas fa-image",
        "flatpages.Flatpage":"fas fa-folder-open",

        "socialaccount.socialaccount":"fas fa-id-card",
        "socialaccount.socialtoken":"fas fa-key",
        "socialaccount.socialapp":"fas fa-window-restore",
},
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible"},
}