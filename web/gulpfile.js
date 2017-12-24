var gulp = require('gulp');
var inject = require('gulp-inject');
var watch = require('gulp-watch');

gulp.task('watch', function () {
     watch('./**/*.*', function(){
       gulp.start('index');
     })
});

gulp.task('index', function () {
  var target = gulp.src('./index.html');
  // It's not necessary to read the files (will speed up things), we're only after their paths:
  var sources = gulp.src(['./scripts/**/*.js', './styles/**/*.css'], {read: false});

  return target.pipe(inject(sources))
    .pipe(gulp.dest('.'));
});
