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
    .controller('PublishedPhotosController', function ($window, linksfetcher, versions) {
        var self = this

        self.title = 'Published Photos'
        linksfetcher.getLinks().then(function(links) {
            self.links = links
        })
        versions.getPythonVersion().then(function(versionPython) {
            self.versionPython = versionPython
        })
        versions.getSQLiteVersion().then(function(versionSQLite) {
            self.versionSQLite = versionSQLite
        })
        self.openAll = function() {
            self.links.forEach(function(link) {
                // console.log(link)
                $window.open(link.url, "_blank")
            })
        }
        self.versionAngular = angular.version.full
    })
