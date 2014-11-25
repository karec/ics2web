function customersController($scope,$http) {
    $http.get("http://www.w3schools.com/website/Customers_JSON.php")
    .success(function(response) {$scope.names = response;});
}


function getDatetimeController($scope,$timeout) {
	
	

	var  myHour = function() {
		var d = new Date();
	var h = d.getHours();
	var m = d.getMinutes();

	

  	$scope.date = h+" : "+m;
  	$timeout(myHour, 5000);



	}

	$timeout(myHour, 500);

  
};

