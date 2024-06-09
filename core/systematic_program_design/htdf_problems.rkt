;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |Lab 02 Starter|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #t)))
(require spd/tags)
(require 2htdp/image)

(@assignment labs/lab-02)

;; HtDF Lab, Problem 1

;; PROBLEM:
;;
;; Design a function called square? that consumes an image and determines 
;; whether the image's height is the same as the image's width.
(@problem 1)
(@htdf square?) ;!!!UNCOMMENT this line when you start on this function

(check-expect (square? (square 10 "solid" "red")) true)
(check-expect (square? (rectangle 5 10 "solid" "red")) false)

(define (square? img)
  (= (image-height img) (image-width img)))

;; HtDF Lab, Problem 2

;; PROBLEM:
;; 
;; Design a function named underline that consumes an image 
;; and produces that image underlined by a black line of the same width. 
;; 
;; 
;; For example, 
;; 
;;   (underline (circle 20 "solid" "green"))
;; 
;; should produce
;;
;;   (above (circle 20 "solid" "green")
;;          (rectangle 40 2 "solid" "black"))
(@problem 2)


(check-expect (underline (circle 20 "solid" "green"))
                         (above (circle 20 "solid" "green")
                                (rectangle 40 2 "solid" "black")))
(check-expect (underline (rectangle 50 30 "solid" "blue"))
              (above (rectangle 50 30 "solid" "blue")
                     (rectangle 50 2 "solid" "black")))

(check-expect (underline (square 40 "solid" "red"))
              (above (square 40 "solid" "red")
                     (rectangle 40 2 "solid" "black")))

(check-expect (underline (ellipse 60 30 "solid" "yellow"))
              (above (ellipse 60 30 "solid" "yellow")
                     (rectangle 60 2 "solid" "black")))

(define (underline img)
  (above img
         (rectangle (image-width img) 2 "solid" "black")))



;; HtDF Lab, Problem 3

;; PROBLEM:
;; 
;; A (much too) simple scheme for pluralizing words in English is to add an 
;; s at the end unless the word already ends in s.
;; 
;; Design a function that consumes a string, and adds s to the end unless 
;; the string already ends in s.
(@problem 3)
;(@htdf pluralize) ;!!!

; String => String(define (tall? img)
; pluralize function, if string ends in s, then don't add an s, otherwise add it
; 

(check-expect (pluralize_two "book") "books")

(define (pluralize_two str)
  (if (string=? (substring str (- (string-length str) 1)) "s")
      str
      (string-append str "s")))


;; HtDF Lab, Problem 4

;; PROBLEM:
;; 
;; Design a function called nth-char-equal? that consumes two strings 
;; and a natural and produces true if the strings both have length greater 
;; than n and have the same character at position n.
;; 
;; 
;; Note, the signature for such a function is:
;; 
;; (@signature String String Natural -> Boolean)
;; 
;; 
;; The tag and template for such a function are:
;; 
;; (@template-origin String)
;; 
;; (@template (define (nth-char-equal? s1 s2 n)
;;              (... s1 s2 n)))
(@problem 4)
;

(check-expect (nth-char-equal? "abc" "abc" 1) true)  ;; 'b' == 'b'
(check-expect (nth-char-equal? "abc" "adb" 2) false) ;; 'b' != 'd'
(check-expect (nth-char-equal? "abc" "a" 1) false)   ;; s2 is too short
(check-expect (nth-char-equal? "a" "abc" 1) false)   ;; s1 is too short
(check-expect (nth-char-equal? "hello" "help" 3) true) ;; 'l' == 'l'

(define (nth-char-equal? s1 s2 n)
  (and
   (>= (string-length s1) (+ n 1))
   (>= (string-length s2) (+ n 1))
   (char=? (string-ref s1 (- n 1)) (string-ref s2 (- n 1)))))


(nth-char-equal? "hello" "help" 3)







