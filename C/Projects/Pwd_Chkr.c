// Import headers
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// This function clears the terminal screen
void clear_screen()
{
    char ch;
    // Clear terminal screen
    ch = getchar();
    getchar(); // Wait for the user to press Enter
    system("clear"); 
}

// This Function checks the passwords' length an updates strength
int check_length(char *pwd, int strgth)
{
    int length = strlen(pwd);

    // Check for password length 
    // Return True if long enough
    if (length >= 8) 
    {
        strgth += 2;
        if (length >= 12) 
        {
            strgth += 2;
        }
    }
    // Return False if not long enough
    else
    {
        printf("\nThe password is not long enough!\n");
        printf("Make sure the password is at least 8 characters long.\n");
    }

    return strgth;
}

// This function checks for the types of characters in the password and updates strength
int check_char(char *pwd, int strgth)
{
    int hasLower = 0, hasUpper = 0, hasDigit = 0, hasSpecial = 0;

    // Check for character types and add to score
    for (int i = 0; i < strlen(pwd); i++) 
    {
        if (pwd[i] >= 'a' && pwd[i] <= 'z') 
        {
            hasLower += 1;
        } 

        else if (pwd[i] >= 'A' && pwd[i] <= 'Z') 
        {
            hasUpper += 1;
        } 

        else if (pwd[i] >= '0' && pwd[i] <= '9') 
        {
            hasDigit += 1;
        } 

        else if (pwd[i] >= '!' && pwd[i] <= '/')
        {
            hasSpecial += 1;
        }

        else if (pwd[i] >= '[' && pwd[i] <= '_')
        {
            hasSpecial += 1;
        }

        else if (pwd[i] >= ':' && pwd[i] <= '?')
        {
            hasSpecial += 1;
        }
        else if (pwd[i] >= '{' && pwd[i] <= '~')
        {
            hasSpecial += 1;
        }
    }
    // Print appropriate message for missing character types
    if(hasLower == 0)
    {
        printf("\nThe password does not contain any lowercase letters.\n");
        printf("Add more lowercase letters to increase password strength.\n");
    }

    if(hasUpper == 0)
    {
        printf("\nThe password does not contain any uppercase letters.\n");
        printf("Add more uppercase letters to increase password strength.\n");
    }

    if(hasDigit == 0)
    {
        printf("\nThe password does not contain any digits.\n");
        printf("Add more digits to increase password strength.\n");
    }

    if(hasSpecial == 0)
    {
        printf("\nThe password does not contain any special characters.\n");
        printf("Add more special characters to increase password strength.\n");
    }

    // Update strength based on character types
    return strgth += hasLower + hasUpper + hasDigit + hasSpecial;
}

// This Function checks your password strength score value and prints the appropriate message
char *check_score(int str_val)
{
    char *strength;
    // Check passowrd strength based on score
    if(str_val < 10)
    {
        printf("\nYour password strength is poor.\n");
        strength = "poor";
    }
    
    else if(str_val >= 10 && str_val < 20)
    {
        printf("\nYour password strength is moderate.\n");
        strength = "moderate";
    }

    else if (str_val >= 20)
    {
        printf("\nYour password strength is excellent.\n");
        strength = "excellent";
    }

    return strength;
}

int main() 
{
    // Initialize vars, arrays
    const int SIZE = 100;
    char password1[100];
    int list_score[10];
    int strength, check = 0, list_index = 0, option;
    // Allocate memory for strings and error check
    char **list_pwd = (char**)malloc(SIZE * sizeof(char)*SIZE);
    // Check if memory failed to allocate
    if (list_pwd == NULL) 
    {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Continuously ask the user for input until they exit
    while(check == 0)
    {
        // Prompt user for menu options
        printf("*** Password Strength Checker Menu ***\n");
        printf("Enter 1 to access the password stength checking program.\n");
        printf("Enter 2 to see the Password Criteria.\n");
        printf("Enter 3 to view past entries and scores.\n");
        printf("Enter 4 to exit the program.\n");
        scanf("%d", &option);
        system("clear"); // Clear terminal screen

        if(option == 1)
        {
            printf("Enter a password: \n");
            scanf("%s", password1);
            if(password1 != NULL)
            {
                // Reset strength to 0 everytime user puts in new password
                strength = 0;
                int i;
                // Calulate strength value
                strength = check_length(password1, strength) + check_char(password1, strength);
                printf("\nPassword strength score: %d\n", strength);
                // Run through user input and copy it to password list
                for (i = 0; i < strlen(password1); i++) 
                {
                    // Allocate memory for each string
                    list_pwd[i] = (char*)malloc((SIZE) * sizeof(char));
                    // Return error if failed to allocate memory
                    if (list_pwd[i] == NULL) 
                    {
                        fprintf(stderr, "Memory allocation failed\n");
                        return 1;
                    }
                    // Put password into the list
                    strncpy(*list_pwd, password1, strlen(password1));
                }
                // Pointer arithmetic used to move along list
                list_pwd += SIZE;
                // Add password strength score to strength list
                list_score[list_index] = strength;
                // Iterate the strength score list
                list_index++;
            }

            printf("Press Enter to continue...\n");
            clear_screen(); 
        }

        else if (option == 2)
        {
            printf("*** Password Criteria ***\n");
            printf("1. Must be more than 8 characters long.\n");
            printf("2. Must contain lowercase characters.\n");
            printf("3. Must contain uppercase characters.\n");
            printf("4. Must contain digits.\n");
            printf("5. Must contain special characters.\n");
            printf("Press Enter to continue...\n");
            clear_screen();
        }
        
        else if (option == 3)
        {
            if (*list_score != NULL)
            {
                // Move pointer back to index 0
                list_pwd -= (SIZE * list_index);
                for(int i = 0; i < list_index; i++)
                {
                    printf("Password: %s\n", *list_pwd);
                    printf("Score: %d\n", list_score[i]);
                    // Move pointer up to next block
                    list_pwd += SIZE;
                }
                printf("Press Enter to continue...\n");
                clear_screen(); 
            }
            else
            {
                printf("No Passwords saved in list yet.\n");
                printf("Press Enter to continue...\n");
                clear_screen(); 
            }
        }

        else if (option == 4)
        {
            printf("Exiting program...\n");
            check = 1; // Ensure to exit loop
        }
    }
    return 0;
}