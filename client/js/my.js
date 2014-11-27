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
				// console.log("test");
				var myCurrent = function(){
					// console.log(len);
					// console.log(tmp);
					if (tmp < 0) {tmp = len};
					$scope.cur_eve = response.current_events[tmp --];
					// console.log(tmp);
				
					$timeout(myCurrent, 5000);
				}
				$timeout(myCurrent, 100);
			}else {
				$scope.cur_eve = response.current_events;
			};
	
		});
	}

	function icsPersoCtrl($scope, $http, $timeout) {
		$http.get("http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics")
		.success(function(response) {
			var len = response.current_events.length -1;
			var tmp = len;
			if (response.current_events.length > 1) {
				// console.log("test");
				var myCurrent = function(){
					// console.log(len);
					// console.log(tmp);
					if (tmp < 0) {tmp = len};
					$scope.cur_eve = response.current_events[tmp --];
					// console.log(tmp);
				
					$timeout(myCurrent, 5000);
				}
				$timeout(myCurrent, 100);
			} else {
				$scope.cur_eve = response.current_events;
			};

				
		});
		
	}

	function icsNextCtrl($scope, $http, $timeout) {
		$http.get("http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics")
		.success(function(response) {

			//console.log(response.current_events.length);
			var len = response.next_events.length -1;
			var tmp = len;
			var tab = [];
			//var name = response.next_events.name;
			var elem = document.getElementsByClassName("next");

			var myNext = function() {
				for (var i = 0; i < len; i++) {
					tab[i] = response.next_events[i]
					var name = response.next_events[i].name;
					console.log(name);
					elem[i].className += "toto";
					$timeout(myNext, 100);
					
				};
			}
			$timeout(myNext, 100);
			$scope.next_eve = tab;

			
			// if (response.next_events.length > 1) {
			// 	// console.log(response.next_events);
			// 	var myNext = function(){
			// 		console.log(len);
			// 		console.log(tmp);
			// 		if (tmp < 0) {tmp = len};
			// 		$scope.next_eve = response.next_events[tmp --];
			// 		console.log($scope.next_eve);
				
			// 		$timeout(myNext, 1000);
			// 	}
			// 	$timeout(myNext, 100);
			// };
	
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

