HereIAm -- Beacon-Based Class Attendance Solution
=================================================

Have a beacon in your class, and when the students come in range, they can sign in on their phones (except the beacon but doesn't quite work yet...).

Three parts:
 - Android app for students (requires Android 4.3+)
 - Android app for the lecturer/manager
 - Server

Note that the server's hostname is hardcoded in the two apps, so you'll need to change it if you want to try it! (The current hostname will have been reused for something else.)

Student App
-----------

Run the android project HereIAm.

Manager App
-----------

Run the android project HereIAmManager.

Server
------

    cd server
    python server.py <some_dir>

where `<some_dir>` is the directory to store the registrations in. (Database? Who needs a database?)

The server binds to port 80 (due to restrictions on Eduroam), so you'll either need to run it as root (not recommended), or else do `sudo setcap 'cap_net_bind_service=+ep' "$(readlink -f "$(which python)")"` so non-privileged processes can bind to port 80.
