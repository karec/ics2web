var app = angular.module('icstoweb', []);


var ics = "http://ics.evalette.net/api/get?url=www.google.com/calendar/ical/valett_e%40etna-alternance.net/private-dcbad4791bccb7846db0fdd38f9498f8/basic.ics"



app.controller('icsObjectController', function($scope, $http) {
	$http.get(ics)
	.success(function(response) {$scope.ics = response;
				
	});
		
	});

app.controller('icsCurrentCtrl', function($scope, $http, $timeout) {
		$http.get(ics)
		.success(function(response) {

			//console.log(response.current_events.length);
			var len = response.current_events.length -1;
			var tmp = len;
			if (response.current_events.length >= 2) {
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
				$scope.cur_eve = response.current_events[0];
				
			}
	
		});
	});


	 app.controller('icsNextCtrl', function($scope, $http, $timeout) {
		$http.get(ics)
		.success(function(response) {
			var len = response.next_events.length -1;
			var tmp = len;
			var tab = [];

			var myNext = function() {

				while (len > 0){
					for (var i = 0; i < 4; i++) {
					tab[i] = response.next_events[i];
	
					
					};

				}
				
				//$timeout(myNext, 1000);
			}
			$timeout(myNext, 100);
			$scope.next_eve = tab;
			var lentab = response.next_events.length -1;
			$scope.lentab = lentab;
		});
	});





 app.controller('getDatetimeController', function($scope,$timeout) {
	var  myHour = function() {
	var d = new Date();
	var t = d.toLocaleTimeString();
  	$scope.date = t;
  	$timeout(myHour, 500);
	}

	$timeout(myHour, 500);
});

app.filter('slice', function() {
  return function(arr, start, end) {
    return arr.slice(start, end);
  };
});

