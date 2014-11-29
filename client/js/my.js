var app = angular.module('icstoweb', []);


var ics = "http://ics.evalette.net/api/get/?url=https://www.google.com/calendar/ical/bene_t%40etna-alternance.net/private-ebd8846b2fae995953df0e5494323e82/basic.ics"




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


app.controller('icsNextCtrl', function($scope, $http, $timeout, $interval) {

	$scope.next_eve = [];
	$scope.tmp = [];
	$scope.tmp_len = 0;
	$scope.init = function () {
		$http.get(ics).then(function (response) {
			events = response.data.next_events;
			st = 0;
			$interval(function () {
				if (st >= events.length - 1) {
					st = 0;
				}
				if (st + 4  > events.length - 1)
					$scope.next_eve = events.slice(st);
				else
					$scope.next_eve = events.slice(st, 4);
				st += 4;
			}, 4000);
		});


	};
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

