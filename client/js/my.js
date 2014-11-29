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


	 app.controller('icsNextCtrl', function($scope, $http, $timeout) {
		$http.get(ics)
		.success(function(response) {
			var len = response.next_events.length;
			var tmp = len;
			var tab = [];

			var myNext = function() {


				function sleep(milliseconds) {
					console.log("Im on sleep");
				  var start = new Date().getTime();
				  for (var i = 0; i < 1e7; i++) {
				    if ((new Date().getTime() - start) > milliseconds){
				      break;
				    }
				  }
				}

				while (len > 0){

					var iter = 4

					var offset = 0;
					for (var i = offset; i < iter; i++) {
					tab[i] = response.next_events[i];
	
					
					};
					$scope.next_eve = tab;
					console.log($scope.next_eve);
					offset = offset + iter;
					console.log("offset "+offset);
					len = len - 4;
					console.log("new len "+len);
					if (len < 4) {iter = len};
					console.log("new iter "+iter);
					sleep(2000);
				}
				
				//$timeout(myNext, 5000);
			}
			$timeout(myNext, 100);
			
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

