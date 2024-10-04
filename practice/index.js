// function outer_function(){
//     let outer_value= "Tanisha"

//     function innerfunction(){
//         console.log(outer_value)
    
//     }    
// return innerfunction;
// }

// const outervalue= outer_function()
// outervalue()


// const data1 = {
//     name:"dfsh",mark:80,
//     name:"gol",mark:99,

//     name:"hell",mark:100,

// }
// console.log(data1)


// function countValidTeams(skills, minPlayers, minLevel, maxLevel) {
//     // Step 1: Filter skills within the range [minLevel, maxLevel]
//     const validSkills = skills.filter(skill => skill >= minLevel && skill <= maxLevel);

//     // Step 2: Initialize count of valid teams
//     let totalTeams = 0;

//     // Step 3: Define a recursive function to generate combinations
//     function generateTeams(index, currentTeam) {
//         // Check if current team is of required length
//         if (currentTeam.length === minPlayers) {
//             // Check if all skills in the current team are valid
//             if (currentTeam.every(skill => skill >= minLevel && skill <= maxLevel)) {
//                 totalTeams++;
//             }
//             return;
//         }

//         // Iterate over remaining elements to form the team
//         for (let i = index; i < validSkills.length; i++) {
//             // Recursively generate teams including the current skill
//             generateTeams(i + 1, [...currentTeam, validSkills[i]]);
//         }
//     }

//     // Start generating teams from the beginning of validSkills array
//     generateTeams(0, []);

//     // Return the total number of valid teams found
//     return totalTeams;
// }

// // Example usage:
// const skills = [4, 4, 8, 5, 6, 1, 5, 7];
// const minPlayers = 3;
// const minLevel = 4;
// const maxLevel = 10;

// const result = countValidTeams(skills, minPlayers, minLevel, maxLevel);
// console.log("Total number of valid teams:", result);  // Expected output: 3






function countValidTeamsForMultipleCases(cases, minPlayers, minLevel, maxLevel) {
    // Function to count valid teams for a single skills array
    function countValidTeams(skills, minPlayers, minLevel, maxLevel) {
        // Step 1: Sort and filter skills within the range [minLevel, maxLevel]
        const validSkills = skills.filter(skill => skill >= minLevel && skill <= maxLevel).sort((a, b) => a - b);

        // Step 2: Initialize count of valid teams
        let totalTeams = 0;

        // Step 3: Define a recursive function to generate combinations
        function generateTeams(index, currentTeam) {
            // Check if current team is of required length
            if (currentTeam.length === minPlayers) {
                // Check if all skills in the current team are valid
                if (currentTeam.every(skill => skill >= minLevel && skill <= maxLevel)) {
                    totalTeams++;
                }
                return;
            }

            // Iterate over remaining elements to form the team
            for (let i = index; i < validSkills.length; i++) {
                // To avoid counting the same combination multiple times,
                // skip duplicates when they appear consecutively in the sorted array
                if (i > index && validSkills[i] === validSkills[i - 1]) continue;
                // Recursively generate teams including the current skill
                generateTeams(i + 1, [...currentTeam, validSkills[i]]);
            }
        }

        // Start generating teams from the beginning of validSkills array
        generateTeams(0, []);

        // Return the total number of valid teams found
        return totalTeams;
    }

    // Array to store results for each case
    const results = [];

    // Iterate over each case and calculate the valid teams
    for (const skills of cases) {
        const result = countValidTeams(skills, minPlayers, minLevel, maxLevel);
        results.push(result);
    }

    // Return the results array containing counts of valid teams for each case
    return results;
}

// Example usage:
const cases = [
    [6, 6, 4, 8, 7, 5, 2, 2, 3, 10],
    [4, 4, 8, 5, 6, 1, 5, 7]
];
const minPlayers = 3;
const minLevel = 4;
const maxLevel = 10;

const results = countValidTeamsForMultipleCases(cases, minPlayers, minLevel, maxLevel);
console.log("Total number of valid teams for each case:", results);  // Expected output: [26, 10]









