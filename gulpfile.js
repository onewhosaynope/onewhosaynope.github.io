var gulp = require('gulp');
var sass = require('gulp-sass');
var minify = require('gulp-minify');
var cleanCSS = require('gulp-clean-css');
var concat = require('gulp-concat');


//sass
gulp.task('compile-sass', () => {
    gulp.src(['public/scss/*.scss', 'public/scss/**/*.scss'])
        .pipe(sass({ outputStyle: 'compressed' }))
        .pipe(gulp.dest('public/gulp/css'));
});


gulp.task('minify-css', () => {
    return gulp.src('public/gulp/css/*.css')
        .pipe(cleanCSS({ compatibility: 'ie8' }))
        .pipe(gulp.dest('public/gulp/css/minify'));
});


gulp.task('minify-js', () => {
    return gulp.src(['public/js/*.js', 'public/js/**/*.js'])
        .pipe(minify({
            ext: {
                min: '.min.js'
            },
            ignoreFiles: ['-min.js']
        }))
        .pipe(gulp.dest('public/gulp/js'))
});


gulp.task('concat-js', () => {
    gulp.src(['public/gulp/js/*.min.js', 'public/gulp/js/**/*.min.js'])
      .pipe(concat('all.min.js'))
      .pipe(gulp.dest('public/gulp/js/minify'))
  });


// Default task
gulp.task('build', gulp.parallel(
    'compile-sass', 'minify-css', 'minify-js', 'concat-js'
));