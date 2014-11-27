function icsObjectController($scope, $http) {
	$http.get("http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics")
	.success(function(response) {$scope.ics = response;
				
	});
		
	}

	function icsCurrentCtrl($scope, $http, $timeout) {
		$http.get("http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics")
		.success(function(response) {

			//console.log(response.current_events.length);
			var len = response.current_events.length -1;
			var tmp = len;
			if (response.current_events.length > 1) {
				console.log("test");
				var myCurrent = function(){
					console.log(len);
					console.log(tmp);
					if (tmp < 0) {tmp = len};
					$scope.cur_eve = response.current_events[tmp --];
					console.log(tmp);
				
					$timeout(myCurrent, 5000);
				}
				$timeout(myCurrent, 100);
			};
	
		});
	}

	function icsObjectController($scope, $http) {
	$http.get("http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics")
	.success(function(response) {$scope.ics = response;
				
	});
		
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

