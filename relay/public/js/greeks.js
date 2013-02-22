// var __proxy = 'requests/proxy.php?__url=http://www.vtrelaycandles.org';
var __proxy = window.location.host == 'localhost'  ? 'requests/proxy.php?__url=http://localhost:8000' : '';

var info = "";

//Feedback slide up

function sortResult(data) {
    data = data.sort(function (a, b) {
        var prop = "company_candles_total";
        if(b[prop] instanceof String){
            a[prop] = a[prop].toLowerCase();
            b[prop] = b[prop].toLowerCase();
        }
        if(b[prop] > a[prop]){return 1;}
        if(b[prop] < a[prop]){
            return -1;}
        else{
            return (compareThings(a["company_name"], b["company_name"]));
        }

       // return (compareThings(b["team_candles_total"], a["team_candles_total"]));
    });
    setupTable(data);
    info = data;
}


$(document).ready(function () {
    $("#feedbackTab").click(function (event) {
        if ($("#feedbackBody").hasClass("up")) {
            $("#feedbackBody").slideUp();
            $("#feedbackBody").removeClass("up");
        }
        else {
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




$(document).ready(function ($) {
jQuery.expr[":"].contains = jQuery.expr.createPseudo(function(arg) {
    return function( elem ) {
        return jQuery(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
  });
  function listFilter(list) {
    var input = $("#searchBox");

    $(input)
      .change( function () {
        var filter = $(this).val();
        if(filter) {
          $('tr').find("td:not(:Contains(" + filter + "))").parent().hide();
          $('tr').find("td:Contains(" + filter + ")").parent().show();
        } else {
          $('tr').show();
        }
        return false;
      })
    .keyup( function () {
        $(this).change();
    });
  }

  $(function () {
    listFilter($(".greekRow"));
  });
}(jQuery));


			//Column sorting
$(function() {
    $('#sorterHeader tr th').click(function() {
        var id = $(this).attr('id');
        var asc = (!$(this).attr('asc')); // switch the order, true if not set

        // set asc="asc" when sorted in ascending order
        $('#sorterHeader tr th').each(function() {
            $(this).removeAttr('asc');
        });
        if (asc) $(this).attr('asc', 'asc');

        sortResults(id, asc);
    });

});

function sortResults(prop, asc) {
    arr = info;

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
                return (compareThings(a.get("company_name"), b.get("company_name")));
            }
        } else {
            if (thing2 > thing1) {
                return 1;
            }
            if (thing2 < thing1) {
                return -1;
            } else {
                return (compareThings(a.get("company_name"), b.get("company_name")));
            }
        }
    });

    showResults(arr);
}

function compareThings(thing1, thing2) {
    if(thing1 instanceof String){
        thing1 = thing1.toLowerCase();
        thing2 = thing2.toLowerCase();
    }
	if(thing1 < thing2){
		return -1;}
	else{
		return 1;}
}

function showResults (arr) {
    var html = '';

    $('#team_table_body').html(
                _.template($('#companies-list-row-template').html(),
                    {companies: arr}));
}

// #
// Default route
CompaniesListView = Backbone.View.extend({
	el: $('#team_table_body'),
	render: function(){
		var that = this;

		$(this.el).empty();
		$('#content').empty();
		$('#loadingImg').show();
		$('#company_name').text('Company Name');
		$('#pagesHeaderTxt').text('Greeks');
		$('#search-area, #sorterHeader, #forScroll, #greekPagesCheck').show();

		CompaniesCollection.fetch({
			success: function(companies){
				$("#loadingImg").hide();

				$(that.el).html(
					_.template($('#companies-list-row-template').html(),
						{companies: companies.models}));

				info = _.toArray(companies.models);
				jQuery("#forScroll").mCustomScrollbar("update");
			}
		});
	}
});

// #/company/:id
// View for the teams in a company
CompanyTeamsListView = Backbone.View.extend({
	el: $('#team_table_body'),
	render: function(id){
		var that = this;

		$(this.el).empty();
		$('#content').empty();
		$('#loadingImg').show();
		$('#company_name').text('Team Name');
		$('#search-area, #sorterHeader, #forScroll, #greekPagesCheck').show();

		var c = new Company({id: id});
		c.fetch({
			success: function(){

				$('#pagesHeaderTxt').html(
					_.template($('#company-title-template').html(), {
						company: c
					}));

				CompanyTeamsCollection.company_id = id;
				CompanyTeamsCollection.fetch({
					success: function(teams){
						$('#loadingImg').hide();

						$(that.el).html(
							_.template($('#teams-list-row-template').html(), {
								teams: teams.models
							}));
						info = _.toArray(teams.models);
						    jQuery("#forScroll").mCustomScrollbar("update");
					}
				});
			}
		});
	}
});

// #/team/:id
// View for listing participants in a team
ParticipantsListView = Backbone.View.extend({
	el: $('#team_table_body'),
	render: function(id){
		var that = this;

		$(this.el).empty();
		$('#content').empty();
		$('#loadingImg').show();
		$('#company_name').text('Participant Name');
		$('#search-area, #sorterHeader, #forScroll, #greekPagesCheck').show();

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
		$('#search-area, #sorterHeader, #forScroll, #greekPagesCheck').hide();
		P.fetch({
			success: function(participant){

				$('#loadingImg').hide();

				vars = {
					id: id,
					participant: participant
				};

				$('#pagesHeaderTxt').html(
					_.template($('#participant-title-template').html(), vars));

				$(that.el).html(
					_.template($('#participant-single-template').html(), vars));

                                            jQuery(".forScroll").mCustomScrollbar("update");
			}
		});

	}
});


Participant = Backbone.Model.extend({
	url: function(){
		return __proxy + '/participants/specific/greek/' + this.id + '/';
	}
});

Team = Backbone.Model.extend({
	url: function(){
		return __proxy + '/team/singular/greek/' + this.id + '/';
	}
});

Teams = Backbone.Collection.extend({
	url: function(){
		return __proxy + '/company/specific/greek/' + this.company_id + '/';
	},
	model: Team,
	company_id: 0,
});


TeamParticipants = Backbone.Collection.extend({
	url: function(){
		return __proxy + '/team/specific/greek/' + this.team_id + '/';
	},
	team_id: 0,
	model: Participant
});

Company = Backbone.Model.extend({
        url: function(){
            return __proxy + '/company/singular/greek/' + this.id + '/';
        }
});

Companies = Backbone.Collection.extend({
	url: __proxy + '/companies/greek/candles/all/',
	model: Company
});

var CompaniesCollection = new Companies();
var CompanyTeamsCollection = new Teams();
// var TeamsCollection = new Teams();
var TeamParticipantsCollection = new TeamParticipants();

var AppRouter = Backbone.Router.extend({
	routes: {
		// 'participants': 'getParticipants',
		'participant/:id': 'getParticipant',
		'team/:id': 'getParticipants',
		// 'teams': 'getTeams',
		'company/:id': 'getCompanyTeams',
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

app_router.on('route:getCompanyTeams', function(id){
	var company_teams_list_view = new CompanyTeamsListView();
	company_teams_list_view.render(id);
});

app_router.on('route:defaultRoute', function(){
	var company_list_view = new CompaniesListView();
	company_list_view.render();
});

// Start Backbone history a necessary step for bookmarkable URL's
Backbone.history.start();