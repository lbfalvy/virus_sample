### Progress:
The first 200 lines essentially obscure string segments by putting them in a base64 encoded table which is rotated by -382, and providing a function to read them. The function is always called on a single string literal.
These are now replaced in the source.