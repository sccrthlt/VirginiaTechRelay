

// var __proxy = 'requests/proxy.php?__url=http://www.vtrelaycandles.org';
var __proxy = window.location.host == 'localhost'  ? 'requests/proxy.php?__url=http://localhost:8000' : '';

var info = "";
var __type = "team";

// Search bar

$(document).ready(function ($) {
    jQuery.expr[":"].contains = jQuery.expr.createPseudo(function (arg) {
        return function (elem) {
            return jQuery(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
        };
    });

    function listFilter(list) {
        var input = $("#searchBox");

        $(input)
            .change(function () {
            var filter = $(this).val();
            if (filter) {
                $('tr').find("td:not(:Contains(" + filter + "))").parent().hide();
                $('tr').find("td:Contains(" + filter + ")").parent().show();
                //$("#forScroll").mCustomScrollbar("update");
            } else {
                $('tr').show();
            }
            //$("#forScroll").mCustomScrollbar("update");
            return false;
        })
            .keyup(function () {
            $(this).change();
        });
    }

    $(function () {
        listFilter($(".teamRow"));
    });
}(jQuery));

//Feedback slide up

$(document).ready(function () {
    //$(":not('#feedbackTab')").click(function () {
    //    $("#feedbackBody").slideDown();
    //});
    $("#feedbackTab").click(function (event) {
        if ($("#feedbackBody").hasClass("up")) {
            $("#feedbackBody").slideUp();
            $("#feedbackBody").removeClass("up");
        } else {
            $("#feedbackBody").slideDown();
            $("#feedbackBody").addClass("up");
        }
        event.stopPropagation();
    });
    $("#feedbackBody").click(function (event) {
        event.stopPropagation();
    });
    $("body").click(function (event) {
        event.stopPropagation();
        if ($("#feedbackBody").hasClass("up")) {
            $("#feedbackBody").slideUp();
            $("#feedbackBody").removeClass("up");
        }
    });
});

function sendemail() {
    p = document.getElementById("problemIn").value;
    e = document.getElementById("emailIn").value;
    $.post("mail.php", {
        problem: p,
        email: e
    },

    function () {
        alert("Thank You for your Feedback!");
        resetFeedback();
    });
}

function sendComment() {
    c = document.getElementById("commentIn").value;
    $.post("comment.php", {
        comment: c
    },

    function () {
        alert("Thank You for your Feedback!");
        resetFeedback();
    });
}

function resetFeedback() {
    document.getElementById("commentIn").value = "";
    document.getElementById("problemIn").value = "";
    document.getElementById("emailIn").value = "";
    $("#feedbackBody").slideUp();
    $("#feedbackBody").removeClass("up");
}

//Column sorting

$(function () {
    $('#sorterHeader tr th').click(function () {
        var id = $(this).attr('id');
        var asc = (!$(this).attr('asc')); // switch the order, true if not set

        // set asc="asc" when sorted in ascending order
        $('#sorterHeader tr th').each(function () {
            $(this).removeAttr('asc');
        });
        if (asc) $(this).attr('asc', 'asc');

        sortResults(id, asc);
    });

});


var __sortFields = {
    team: {
        sort_name: "team_name",
        sort_donations: "team_donation_milestone_candles",
        sort_events: "team_event_milestone_candles",
        sort_emails: "team_email_milestone_candles",
        sort_total: "team_candles_total",
    },
    participant: {
        sort_name: "participant_first_name",
        sort_donations: "participant_donation_milestone_candles",
        sort_registration: "participant_registration_milestone_candles",
        sort_events: "participant_event_milestone_candles",
        sort_emails: "participant_email_milestone_candles",
        sort_total: "participant_candles_total",
    }
}

function sortResults(prop, asc) {
    arr = info;

    var __name = __sortFields[__type].sort_name;

    prop = __sortFields[__type][prop];

    arr = arr.sort(function (a, b) {
        var thing1 = a.get(prop);
        var thing2 = b.get(prop);

        if (thing1 instanceof String) {
            thing1 = thing1.toLowerCase();
            thing2 = thing2.toLowerCase();
        }
        if (asc) {
            if (thing1 > thing2) {
                return 1;
            }
            if (thing1 < thing2) {
                return -1;
            } else {
                return (compareThings(a.get(__name), b.get(__name)));
            }
        } else {
            if (thing2 > thing1) {
                return 1;
            }
            if (thing2 < thing1) {
                return -1;
            } else {
                return (compareThings(a.get(__name), b.get(__name)));
            }
        }
    });

    showResults(arr);
}


function compareThings(thing1, thing2) {
    if (thing1 instanceof String) {
        thing1 = thing1.toLowerCase();
        thing2 = thing2.toLowerCase();
    }
    if (thing1 < thing2) {
        return -1;
    } else {
        return 1;
    }
}

function showResults(arr) {
    var html = '';

    if ( __type == "team" ) {
	    $('#teamList_body').html(
	                _.template($('#teams-list-row-template').html(),
	                    {teams: arr}));
    } else if ( __type == "participant" ) {
	    $('#teamList_body').html(
	                _.template($('#participants-list-row-template').html(),
	                    {participants: arr}));
    }
}

// #
// Default route
TeamsListView = Backbone.View.extend({
	el: $('#teamList_body'),
	render: function(){
		var that = this;

		$(this.el).empty();
		$('#content').empty();
		$('#loadingImg').show();
		$('#team_name').text('Team Name');
		$('#pagesHeaderTxt').text('General Teams');
		$('#search-area, #sorterHeader, #forScroll, #pagesCheck').show();
		__type = "team";

		TeamsCollection.fetch({
			success: function(teams){
				$("#loadingImg").hide();

				$(that.el).html(
					_.template($('#teams-list-row-template').html(),
						{teams: teams.models}));

				info = _.toArray(teams.models);
				// console.log(info);
				jQuery("#forScroll").mCustomScrollbar("update");
			}
		});
	}
});

// #/team/:id
//View for listing participants in a team
ParticipantsListView = Backbone.View.extend({
	el: $('#teamList_body'),
	render: function(id){
		var that = this;

		$(this.el).empty();
		$('#content').empty();
		$('#loadingImg').show();
		$('#team_name').text('Participant Name');
		$('#search-area, #sorterHeader, #forScroll, #pagesCheck').show();
		__type = "participant";

		var t = new Team({id: id}).fetch({
			success: function(team){

				$('#pagesHeaderTxt').html(
					_.template($('#participants-title-template').html(), {
						team: team
					}));

				TeamParticipantsCollection.team_id = id;
				TeamParticipantsCollection.fetch({
					success: function(participants){
						$('#loadingImg').hide();

						$(that.el).html(
							_.template($('#participants-list-row-template').html(), {
								participants: participants.models
							}));
						info = _.toArray(participants.models);
						jQuery("#forScroll").mCustomScrollbar("update");
					}
				});
			}
		});
	}
});

// #/participant/:id
// View of a single participant
ParticipantSingleView = Backbone.View.extend({
	el: $('#content'),
	render: function(id){
		var that = this;
		var P = new Participant({id: id});
		$('#search-area, #sorterHeader, #forScroll, #pagesCheck').hide();
		//jQuery(".forScroll").mCustomScrollbar("destroy");
		P.fetch({
			success: function(participant){

				$('#loadingImg').hide();

				vars = {
					id: id,
					participant: participant
				};

                                            _.defer(function(){

                                                $('#pagesHeaderTxt').html(
                                                    _.template($('#participant-title-template').html(), vars));

                                                $(that.el).html(
                                                    _.template($('#participant-single-template').html(), vars));

                                            });

                                            _.defer(function(){
                                                //jQuery(".forScroll").mCustomScrollbar();
                                            });
			}
		});

	}
});


Participant = Backbone.Model.extend({
	url: function(){
		return __proxy + '/participants/specific/' + this.id + '/';
	}
});

Team = Backbone.Model.extend({
	url: function(){
		return __proxy + '/teams/singular/' + this.id + '/';
	}
});

Teams = Backbone.Collection.extend({
	url: __proxy + '/teams/candles/all/',
	model: Team
});


TeamParticipants = Backbone.Collection.extend({
	url: function(){
		return __proxy + '/team/specific/general/' + this.team_id + '/';
	},
	team_id: 0,
	model: Participant
});


var TeamsCollection = new Teams();
var TeamParticipantsCollection = new TeamParticipants();

var AppRouter = Backbone.Router.extend({
	routes: {
		// 'participants': 'getParticipants',
		'participant/:id': 'getParticipant',
		'team/:id': 'getParticipants',
		'teams': 'getTeams',
		'*actions': 'defaultRoute'
	}
});

var app_router = new AppRouter();

app_router.on('route:getParticipant', function(id){
	var participant_single_view = new ParticipantSingleView();
	participant_single_view.render(id);
});

app_router.on('route:getParticipants', function(id){
	var participants_list_view = new ParticipantsListView();
	participants_list_view.render(id);
});

app_router.on('route:defaultRoute', function(){
	var teams_list_view = new TeamsListView();
	teams_list_view.render();
});

// Start Backbone history a necessary step for bookmarkable URL's
Backbone.history.start();