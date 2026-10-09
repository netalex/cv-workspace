var gulp = require('gulp'),
    jade = require('gulp-jade'),
    sass = require('gulp-ruby-sass'),
    browserSync = require('browser-sync').create(),
    cp = require('child_process');

// Build Jekyll site
gulp.task('jekyll-build', function (done){
  return cp.spawn('jekyll.bat', ['build'], {stdio: 'inherit'})
        .on('close', done);
});

// Rebuild Jekyll site
gulp.task('jekyll-rebuild', ['jekyll-build'], function(){
  browserSync.reload();
});

// Compile HTML files to Jade
gulp.task('jade', function(){
  return gulp.src('jade/*.jade')
        .pipe(jade({ pretty: true }))
        .pipe(gulp.dest('_includes/'))
});

// Compile SASS files to CSS
gulp.task('sass', function(){
  return sass('sass/*.sass', {sourcemap: true})
        .pipe(gulp.dest('_site/css'))
        .pipe(browserSync.stream()) // We can use this to inject changed files to browserSync
        .pipe(gulp.dest('css/'))
});

// Watch changes for the files and execute compilations and 'jekyll-rebuild'
gulp.task('watch', function(){
  gulp.watch('sass/*.sass', ['sass']);
  gulp.watch('jade/*jade', ['jade']);
  gulp.watch(['_includes/*.html', 'css/*.css'], ['jekyll-rebuild']);
});

// Serve a local server with browserSync, going with it is the 'jekyll-build' task
gulp.task('serve', ['jekyll-build'], function() {
    browserSync.init({
        server: "_site/"
    });
});

// This is the default task, just type 'gulp' on your favorite command line
// tool and the site will be built.
gulp.task('default', ['serve', 'watch']);
