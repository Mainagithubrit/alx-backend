import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
	console.log("Redis client not connected to the server: ERROR_MESSAGE", err)
);

client.on("connect", () => {
	console.log("Redis client connected to the server");
});

const setNewSchool = (schoolName, value) => {
	client.SET(schoolName, value, print);
};

async function displaySchoolValue(schoolName) {
	const getAsync = promisify(client.GET).bind(client);
	const value = await getAsync(schoolName);
	console.log(value);
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
