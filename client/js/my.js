function customersController($scope,$http) {
    $http.get("http://www.w3schools.com/website/Customers_JSON.php")
    .success(function(response) {$scope.names = response;});
}

function icsObjectController($scope, $http) {
	$http.get("http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics")
	.success(function(response) {$scope.ics = response;
		
	});

	

	// var now = function(response){
	// 		var d = new Date();
	// 		for (var i = 0; i < response.length; i++) {
	// 			if (response[i].start >= d && d <= response[i].end ) {
	// 				$scope.now = response[i];
	// 		};
	// 		};
		
	}



function getDatetimeController($scope,$timeout) {
	var  myHour = function() {
	var d = new Date();
	var t = d.toLocaleTimeString();
  	$scope.date = t;
  	$timeout(myHour, 500);
	}

	$timeout(myHour, 500);
};

