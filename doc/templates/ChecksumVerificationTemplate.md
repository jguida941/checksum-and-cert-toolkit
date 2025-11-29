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

SHA-256 is a modern SHA-2 hash algorithm that Java supports directly with MessageDigest.getInstance("SHA-256"). It is designed to be collision-resistant, and there are no practical collision attacks known against it. Older algorithms like MD5 and SHA-1 from the same Java standard list have known collision problems, so they are not a good choice for verifying a published public key or file by checksum.

I also considered SHA-512, which has an even bigger safety margin, but it
produces a longer hash value (512 bits instead of 256 bits) that is more than I
need here. SHA-256 is widely used, well supported, and usually faster to
compute than SHA-512, so it gives a good balance of security and performance
for this application.

A collision means two different inputs end up with the exact same hash value.
If collisions were easy to create, an attacker could take a "good" value (like
a real public key or clean file), copy its checksum, and then build a
different, malicious value that still matches that same checksum. The check
would say "everything is fine" even though the data has been swapped. By using
SHA-256, I am using an algorithm where that kind of trick is not realistic for
this project.

## 3. Generate Checksum

You will submit your refactored code to your instructor. Your instructor will
review it and this document.

In my code, I set `DATA = "Justin Guida"`, created a `MessageDigest` instance
with `SHA-256`, called `digest()` on the UTF-8 bytes of that string to get the
hash, then used a `bytesToHex` helper method to convert the hash bytes into a
hex string returned by the `/hash` endpoint.

## 4. Verification
<img width="826" height="382" alt="Screenshot 2025-11-29 at 4 28 00 AM" src="https://github.com/user-attachments/assets/96167256-c698-4424-b73f-6d066f6c8dd8" />
