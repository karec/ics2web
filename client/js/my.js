var app = angular.module('icstoweb', []);


var BASE_URL = "http://ics.evalette.net/api/get/?url=";

function scrollInf() {
	lastElementTop = $('#login').height() ;
	scrollAmount = lastElementTop ;
    $('#login').animate({top: (scrollAmount) * -1}, (15 * scrollAmount), 'swing', function () {
		lastElementTop = $('#login').css('top', '225px');
		scrollInf();
	});
}

app.controller('planning', function ($scope, $http, $timeout, $interval, $location) {

	$scope.$on('onRepeatLast', function (scope, element, attrs) {
		scrollInf();
	});

	var loadData = function () {
		var ics = $scope.url;
		$http.get(ics).then(function (response) {

			$scope.ics = response.data;

			var len = response.data.current_events.length -1;
			var tmp = len;
			if (response.data.current_events.length >= 2) {
				var myCurrent = function(){
					if (tmp < 0) {tmp = len}
					$scope.cur_eve = response.data.current_events[tmp --];
					$timeout(myCurrent, 5000);
				};
				$timeout(myCurrent, 100);
			} else {
				$scope.cur_eve = response.data.current_events[0];
			}
			$scope.next_events = response.data.next_events;
			next_events();

		}, function (error) {
			alert('Error : ' + error);
		});
	};

	$scope.init = function () {
		var url = $location.search().url;
		if (!url) {
			alert('No url provided !');
			return false;
		}
		$scope.url = BASE_URL + url;
		$scope.st = 0;
		loadData();
	};

	var next_events = function () {
		if (!$scope.next_events)
			return false;
		events = $scope.next_events;
		st = $scope.st ? $scope.st : 0;
		if (st > events.length - 1) {
			$scope.st = 0;
			st = 0;
		}
		if (st + 5  > events.length - 1)
			$scope.next_eve = events.slice(st);
		else
			$scope.next_eve = events.slice(st, st + 5);
		$scope.st += 5;


	};

	var myHour;
	myHour = function () {
		var d = new Date();
		$scope.date = d.toLocaleTimeString();
		$timeout(myHour, 500);
	};

	$timeout(myHour, 500);
	$interval(loadData, 50000);
	$interval(next_events, 4000);

});

app.filter('slice', function() {
	return function(arr, start, end) {
		return arr.slice(start, end);
	};
});

app.directive('onLastRepeat', function($timeout) {
	return function(scope, element, attrs) {
		if (scope.$last === true) {
			 $timeout(function () {
                scope.$emit('onRepeatLast', element, attrs);
			 });
		}
	};
});

