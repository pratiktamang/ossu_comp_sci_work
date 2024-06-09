;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Lab 01 Starter|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
;; Intro Lab
(require spd/tags)
(require 2htdp/image)
(@assignment labs/lab-01)

;****************************************************
(@problem 1)
;; As your first task, use string primitives to create an expression tha
;; concatenates prefix and suffix and adds "_" between them
;; (so you get "hello_world" when you run the program) in the starter file.

(define PREFIX "hello")
(define SUFFIX "world")

(string-append PREFIX "_" SUFFIX)

;****************************************************
(@problem 2)
;; Your next task is to use string primitives to create an expression that
;; adds "_" at position i (the position that is i characters from the left
;; of the string). Again, in this particular example, the expected result
;; is "hello_world".


(define STR "helloworld")
(define I 5)
(string-append (substring STR 0 5)
               "_"
               (substring STR 5 (string-length STR)))


;****************************************************
(@problem 3)
;; Create an expression that produces the number of pixels in the CAT image.
(if (< 1 5)
    (> 2 1)
    "yes"
    "no")
(define CAT (bitmap/url "https://cs110.students.cs.ubc.ca/labs/cat.png"))
(* (image-height CAT) (image-width CAT))

;****************************************************
(@problem 4)
;; Create an expression that computes whether the value of CAT is "tall" (height is larger than its width),
;; "wide" (width is larger than its height), or "square" (height is the same as its width).

(cond
  [(> (image-height CAT)(image-width CAT)) "tall"]
  [(< (image-height CAT)(image-width CAT)) "wide"]
  [else "square"])

;****************************************************
(@problem 5)

;; Write an expression that computes whether the first character in the value of STR is "h".
;; If you do not change the constant definition for STR in the starter file, the expected result is true.

(string=? (substring STR 0 1) "h")

