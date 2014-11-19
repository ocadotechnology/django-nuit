var nuit = {};

// Setup Functions

nuit.csrftoken = $.cookie('csrftoken');

nuit.csrfSafeMethod = function(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

nuit.setup = function() {

    // Enable AJAX requests in Django
    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!nuit.csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", nuit.csrftoken);
                xhr.setRequestHeader('Accept', 'application/json');
            }
        }
    });

    // Hightlight current page in menu
    if ($('.nuit-active-menu').length == 0) {
        $($('.breadcrumbs > .menu-item a').get().reverse()).each(function() {
            var matched_links = $(".sidebar.on-left a[href='" + $(this).attr('href') + "']");
            if (matched_links.length != 0) {
                matched_links.parent().addClass('active');
                return false;
            }
        });
    } else {
        $('.nuit-active-menu').each(function() {
            $('.menu-' + $(this).html()).addClass('active');
        });
    }

    // Highlight current breadcrumb
    $('.nuit-breadcrumbs li:last-child').addClass('current');

    // Fix right-menu modals when they're closed
    $(document).on('closed.fndtn.reveal', '[data-reveal]', function () {
        var modal = $(this);
        modal.attr('style', '');
    });

    // Fix right-menu modals on iOS
    $(document).on('click tap touchstart', '.close-reveal-modal', function() {
        return $('[data-reveal]').foundation('reveal', 'close');
    }); 

    // Add correct links for cog-menu
    $('.sidebar.on-right > section').each(function() {
        $this = $(this);
        if ($this.data('reveal') === "") {
            $('#right-menu-drop').append("<li><a href='#' data-reveal-id='" + $this.attr('id') + "'>" + $this.data('link') + "</a></li>");
        } else {
            $nav = $this.find('nav');
            if ($nav.length) {
                $nav.find('ul li').each(function() {
                    $li = $(this);
                    $('#right-menu-drop').append($li.clone());
                });
            }
        }
    });

    // Add left-menu links to application menu on small screens
    $('.sidebar.on-left > section').each(function() {
        $this = $(this);
        $nav = $this.find('nav');
        if ($nav.length) {
            $title = $this.find('h5');
            $append_to = $('#left-menu-drop');
            if ($title.length && !$this.hasClass('main-nav')) {
                $new_li = $('<li></li>').addClass('show-for-small-only').addClass('has-dropdown');
                $new_li.append("<a href='#'>" + $title.html() + "</a>");
                $append_to.append($new_li);
                $new_ul = $("<ul class='dropdown'></ul>");
                $new_li.append($new_ul);
                $append_to = $new_ul;
            }
            $nav.find('ul li').each(function() {
                $li = $(this);
                $append_to.append($li.clone().addClass('show-for-small-only'));
            });
            $('#left-menu-drop').append("<li class='show-for-small-only divider'></li>");
        }
    });

    // Collapseable menu items
    $('.nuit-collapse').click(function() {
        $this = $(this);
        $section = $this.closest('section');
        $content = $section.find('.side-content');
        if ($this.hasClass('nuit-collapsed')) {
            $this.removeClass('nuit-collapsed');
            $section.removeClass('nuit-collapsed');
            $content.slideDown();
        } else {
            $this.addClass('nuit-collapsed');
            $section.addClass('nuit-collapsed');
            $content.slideUp();
        }
    });

    nuit.trigger_button_bars();
    nuit.trigger_responsive_tables();

    // Setup foundation
    $(document).foundation();

};

// User functions

nuit.button_bar_handler = function(e) {
    e.preventDefault();
    e.data.buttons.removeClass('alert');
    $(this).addClass('alert');
    e.data.button_group.trigger('change', $(this).data('value'));
}

nuit.trigger_button_bars = function() {
    $('.button-bar .button-group').each(function() {
        var $button_group = $(this);
        var $buttons = $(this).find('.button');
        $buttons.off('click', nuit.button_bar_handler);
        $buttons.on(
            'click',
            null,
            {
                'buttons': $buttons,
                'button_group': $button_group,
            },
            nuit.button_bar_handler
        );
    });
};

nuit.button_bar_value = function($button_bar, value) {
    if (value === undefined) {
        return $button_bar.find('.button.alert').data('value');
    } else {
        $button_bar.find('.button').each(function() {
            $button = $(this);
            if ($button.data('value') != value) {
                $button.removeClass('alert');
            } else {
                $button.addClass('alert');
            }
        });
    }
};

nuit.trigger_responsive_tables = function() {
    // Set headers for grouped responsive tables
    $('table.responsive.grouped').find('td').each(function() {
        $td = $(this);
        $td.attr('data-title', $td.closest('table').find('th').eq($td.index()).html());
    });
    $('table.responsive.scroll').each(function () {
        $table = $(this);
        classes = 'responsive scroll';
        if ($table.hasClass('medium-down')) {
            classes += ' medium-down';
        }
        $table.wrap('<div class="' + classes + '"></div>');
    });
};

nuit.add_message = function(alert_type, message) {
    message_html = '<div data-alert class="alert-box ' + alert_type.toLowerCase() + '">' + message + '<a href="#" class="close">&times;</a></div>';
    var $message = $(message_html);
    $('.nuit-messages').append($message).foundation('reflow');
};

nuit.confirmation_box = function(user_options) {
    var defaults = {
        title:          'Confirmation required',
        description:    'Are you sure you wish to perform this action?',
        size:           'tiny',
        yes:            'Yes',
        no:             'No',
        on_confirm:     function () { console.log('Confirmed!'); },
        on_abort:       function () { console.log('Aborted!'); },
    };
    var options = $.extend({}, defaults, user_options);

    var modal = $('<div data-reveal></div>')
        .addClass('reveal-modal ' + options.size)
        .append('<h2>' + options.title + '</h2>')
        .append(options.description);

    var confirm_button = $('<a href="#" class="button">' + options.yes + '</a> ');
    var abort_button = $('<a href="#" class="right button alert">' + options.no + '</a>');

    modal.append(confirm_button);
    modal.append(abort_button);

    confirm_button.click(function() {
        modal.foundation('reveal', 'close');
        options.on_confirm();
    });

    abort_button.click(function() {
        modal.foundation('reveal', 'close');
        options.on_abort();
    });

    modal.on('closed.fdntn.reveal', function() {
        $(this).remove();
    });

    $('body').append(modal);
    modal.foundation('reflow').foundation('reveal', 'open');

};

// Initialisation
$(document).ready(function() {
    nuit.setup();
}); 
