                0x03. Queuing System in JS

-   This is backend project that introduces REDIS
-   It has several tasks which include: 0. Install a redis instance - Download, extract, and compile the latest stable Redis version - Start Redis in the background with src/redis-server - Make sure that the server is working with a ping src/redis-cli ping - Using the Redis client again, set the value School for the key Holberton - Kill the server with the process id of the redis-server (hint: use ps and grep) - Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.

        1. Node Redis Client
            - Install node_redis using npm
            - Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:
                - It should log to the console the message Redis client connected to the server when the connection to Redis works correctly.
                - It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work

        2. Node Redis client and basic operations
            - In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).
            - Add two functions:
                - setNewSchool:
                    - It accepts two arguments schoolName, and value.
                    - It should set in Redis the value for the key schoolName.
                    - It should display a confirmation message using redis.print
            - displaySchoolValue:
                - It accepts one argument schoolName.
                - It should log to the console the value for the key passed as argument
            - At the end of the file, call:
                - displaySchoolValue('Holberton');
                - setNewSchool('HolbertonSanFrancisco', '100');
                - displaySchoolValue('HolbertonSanFrancisco');

        3. Node Redis client and async operations
            - In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)
            - Using promisify, modify the function displaySchoolValue to use ES6 async / await

        4. Node Redis client and advanced operations
            - In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value

            # Create Hash:
            - Using hset, let’s store the following:
                - The key of the hash should be HolbertonSchools
                - It should have a value for:
                    - Portland=50
                    - Seattle=80
                    - New York=20
                    - Bogota=20
                    - Cali=40
                    - Paris=2
            - Make sure you use redis.print for each hset

            # Display Hash:
            - Using hgetall, display the object stored in Redis. It should return the following:

            # Requirements
            - Use callbacks for any of the operation, we will look at async operations later

        5. Node Redis client publisher and subscriber
            - In a file named 5-subscriber.js, create a redis client:
                - On connect, it should log the message Redis client connected to the server
                - On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
                - It should subscribe to the channel holberton school channel
                - When it receives message on the channel holberton school channel, it should log the message to the console
                - When the message is KILL_SERVER, it should unsubscribe and quit
            - In a file named 5-publisher.js, create a redis client:
                - On connect, it should log the message Redis client connected to the server
                - On error, it should log the message Redis client not connected to the server: ERROR MESSAGE
                - Write a function named publishMessage:
                    - It will take two arguments: message (string), and time (integer - in ms)
                    - After time millisecond:
                        - The function should log to the console About to send MESSAGE
                        - The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments
                    - At the end of the file, call

            6. Create the Job creator
                - In a file named 6-job_creator.js:
                    - Create a queue with Kue
                    - Create an object containing the Job data with the following format:
                    {
                        phoneNumber: string,
                        message: string,
                    }
                    - Create a queue named push_notification_code, and create a job with the object created before
                    - When the job is created without error, log to the console Notification job created: JOB ID
                    - When the job is completed, log to the console Notification job completed
                    - When the job is failing, log to the console Notification job failed

            7. Create the Job processor
                - In a file named 6-job_processor.js:
                    - Create a queue with Kue
                    - Create a function named sendNotification:
                        - It will take two arguments phoneNumber and message
                        - It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
                - Write the queue process that will listen to new jobs on push_notification_code:
                    - Every new job should call the sendNotification function with the phone number and the message contained within the job data

            8. Track progress and errors with Kue: Create the Job creator
                - In a file named 7-job_creator.js:
                - Create an array jobs with the following data inside:

                const jobs = [
                    {
                        phoneNumber: '4153518780',
                        message: 'This is the code 1234 to verify your account'
                    },
                    {
                        phoneNumber: '4153518781',
                        message: 'This is the code 4562 to verify your account'
                    },
                    {
                        phoneNumber: '4153518743',
                        message: 'This is the code 4321 to verify your account'
                    },
                    {
                        phoneNumber: '4153538781',
                        message: 'This is the code 4562 to verify your account'
                    },
                    {
                        phoneNumber: '4153118782',
                        message: 'This is the code 4321 to verify your account'
                    },
                    {
                        phoneNumber: '4153718781',
                        message: 'This is the code 4562 to verify your account'
                    },
                    {
                        phoneNumber: '4159518782',
                        message: 'This is the code 4321 to verify your account'
                    },
                    {
                        phoneNumber: '4158718781',
                        message: 'This is the code 4562 to verify your account'
                    },
                    {
                        phoneNumber: '4153818782',
                        message: 'This is the code 4321 to verify your account'
                    },
                    {
                        phoneNumber: '4154318781',
                        message: 'This is the code 4562 to verify your account'
                    },
                    {
                        phoneNumber: '4151218782',
                        message: 'This is the code 4321 to verify your account'
                    }

    ];

                - After this array created:
                    - Create a queue with Kue
                    - Write a loop that will go through the array jobs and for each object:
                        - Create a new job to the queue push_notification_code_2 with the current object
                        - If there is no error, log to the console Notification job created: JOB_ID
                        - On the job completion, log to the console Notification job JOB_ID completed
                        - On the job failure, log to the console Notification job JOB_ID failed: ERROR
                        - On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete

            9. Track progress and errors with Kue: Create the Job processor
                - In a file named 7-job_processor.js:
                - Create an array that will contain the blacklisted phone numbers. Add in it 4153518780 and 4153518781 - these 2 numbers will be blacklisted by our jobs processor.
                - Create a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:
                    - When the function is called, track the progress of the job of 0 out of 100
                    - If phoneNumber is included in the “blacklisted array”, fail the job with an Error object and the message: Phone number PHONE_NUMBER is blacklisted
                    - Otherwise:
                        - Track the progress to 50%
                        - Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE
                - Create a queue with Kue that will proceed job of the queue push_notification_code_2 with two jobs at a time.

            10. Writing the job creation function
                - In a file named 8-job.js, create a function named createPushNotificationsJobs:
                    - It takes into argument jobs (array of objects), and queue (Kue queue)
                    - If jobs is not an array, it should throw an Error with message: Jobs is not an array
                    - For each job in jobs, create a job in the queue push_notification_code_3
                    - When a job is created, it should log to the console Notification job created: JOB_ID
                    - When a job is complete, it should log to the console Notification job JOB_ID completed
                    - When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR
                    - When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete

            11. Writing the test for job creation
                - Now that you created a job creator, let’s add tests:
                    - Import the function createPushNotificationsJobs
                    - Create a queue with Kue
                    - Write a test suite for the createPushNotificationsJobs function:
                        - Use queue.testMode to validate which jobs are inside the queue

            12. In stock?
