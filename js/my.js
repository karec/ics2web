function customersController($scope,$http) {
    $http.get("http://www.w3schools.com/website/Customers_JSON.php")
    .success(function(response) {$scope.names = response;});
}


function getDatetimeController($scope,$timeout) {
	
	

	var  myHour = function() {
		var d = new Date();
		d.toLocaleTimeString();
	var h = d.getHours();
	var m = d.getUTCMinutes();
	var t = d.toLocaleTimeString();


	

  	$scope.date = t;
  	$timeout(myHour, 500);



	}

	$timeout(myHour, 500);

  
};

