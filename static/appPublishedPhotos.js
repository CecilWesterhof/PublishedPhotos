angular.module('Published Photos', [])
    .factory('linksfetcher', function($http) {
        var service = {
            getLinks: function() {
                return $http.get('/links/data').then(function(result) {
                    return result.data
                })
            }
        }
        return service
    })
    .factory('versions', function($http) {
        var service = {
            getPythonVersion: function() {
                return $http.get('/versionPython').then(function(result) {
                    return result.data
                })
            },
            getSQLiteVersion: function() {
                return $http.get('/versionSQLite').then(function(result) {
                    return result.data
                })
            }
        }
        return service;
    })
    .controller('PublishedPhotosController', function ($scope, $window, linksfetcher, versions) {
        this.title = 'Published Photos'
        linksfetcher.getLinks().then(function(links) {
            $scope.links = links
        })
        versions.getPythonVersion().then(function(versionPython) {
            $scope.versionPython = versionPython
        })
        versions.getSQLiteVersion().then(function(versionSQLite) {
            $scope.versionSQLite = versionSQLite
        })
        this.openAll = function() {
            $scope.links.forEach(function(link) {
                // console.log(link)
                $window.open(link.url, "_blank")
            })
        }
        this.versionAngular = angular.version.full
    })
