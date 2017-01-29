module.exports = function(grunt) {
	// load all grunt tasks
    require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
        less: {
            dev: {
                options: {
                    sourceMap: true,
                    sourceMapFilename: 'css/main.css.map', // where file is generated and located
                    sourceMapURL: 'main.css.map', // the complete url and filename put in the compiled css file
                },
                files: {
                    'css/main.css': 'less/main.less'
                }
            }
        },
        watch: {
            options: {
                nospawn: true,
                livereload: true
            },
            html: {
                files: ['**/*.html']
            },
            less: {
                files: ['less/**/*.less'],
                tasks: ['less']
            },
            grunt: {
                files: ['Gruntfile.js']
            }
        }
	});
	grunt.registerTask('default', ['watch']);
};