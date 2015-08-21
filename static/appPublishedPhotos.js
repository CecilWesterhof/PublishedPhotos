angular.module('Published Photos', [])
    .factory('linksfetcher', function($http) {
        var service = {
            getLinks: function() {
                return $http.get('/links/data').then(function(result) {
                    return result.data
                });

            }
        };
        return service;
    })
    .controller('PublishedPhotosController', function ($scope, $window, linksfetcher) {
        $scope.title = 'Published Photos'
        linksfetcher.getLinks().then(function(links) {
            $scope.links = links;
        });
        $scope.openAll = function() {
            $scope.links.forEach(function(link) {
                // console.log(link)
                $window.open(link.url, "_blank")
            })
        }
        $scope.getVersion = function() {
            return angular.version.full
        }
    })
