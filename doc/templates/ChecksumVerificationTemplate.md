# CS 305 Module Five Coding Assignment: Checksum Verification Template

## Instructions

Using the instructions from the Module Five Coding Assignment Checksum
Verification Guidelines and Rubric, keep this file with your submission.

## 1. Algorithm Cipher

I recommend using SHA-256 as the MessageDigest algorithm. It is one of the
standard Java Security MessageDigest algorithm names (from Oracle's list), and
it gives a 256-bit hash that is strong enough to avoid collisions for any
realistic use case in this project.

## 2. Justification

SHA-256 is a modern SHA-2 hash algorithm provided by Java
(`MessageDigest.getInstance("SHA-256")`). It is designed to be
collision-resistant, and there are no practical collision attacks known against
it. Legacy algorithms like MD5 and SHA-1 from the same Java standard list are
known to be vulnerable to collisions, so they are not appropriate for verifying
a published public key by checksum.

I also considered SHA-512, which provides an even larger security margin, but
it produces a longer hash value (512 bits vs. 256 bits) that is unnecessary for
this use case. SHA-256 is widely supported and typically faster to compute than
SHA-512, making it a good balance of security and performance for this
application.

## 3. Generate Checksum

You will submit your refactored code to your instructor. Your instructor will
review it and this document.

## 4. Verification

Insert a screenshot below of the secure web browser with your unique
information (data string, algorithm name, and checksum hash value). Replace the
placeholder link with the actual screenshot path committed to this repository.

![Screenshot placeholder](../images/hash-screenshot.png)
