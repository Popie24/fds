#include <iostream>
#include <queue>
#include <string>

class JobQueue {
private:
    std::queue<std::string> jobs;

public:
    // Function to add a job to the queue
    void addJob(const std::string& job) {
        jobs.push(job);
        std::cout << "Job '" << job << "' added to the queue.\n";
    }

    // Function to delete a job from the queue
    void deleteJob() {
        if (jobs.empty()) {
            std::cout << "The job queue is empty. No job to delete.\n";
        } else {
            std::cout << "Job '" << jobs.front() << "' removed from the queue.\n";
            jobs.pop();
        }
    }

    // Function to display all jobs in the queue
    void displayJobs() const {
        if (jobs.empty()) {
            std::cout << "The job queue is empty.\n";
        } else {
            std::queue<std::string> temp = jobs; // Copy to preserve original queue
            std::cout << "Jobs in the queue:\n";
            while (!temp.empty()) {
                std::cout << "- " << temp.front() << '\n';
                temp.pop();
            }
        }
    }
};

int main() {
    JobQueue jobQueue;
    int choice;
    std::string jobName;

    do {
        std::cout << "\n--- Job Queue Menu ---\n";
        std::cout << "1. Add Job\n";
        std::cout << "2. Delete Job\n";
        std::cout << "3. Display Jobs\n";
        std::cout << "4. Exit\n";
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                std::cout << "Enter job name: ";
                std::cin.ignore(); // Clear input buffer
                std::getline(std::cin, jobName);
                jobQueue.addJob(jobName);
                break;

            case 2:
                jobQueue.deleteJob();
                break;

            case 3:
                jobQueue.displayJobs();
                break;

            case 4:
                std::cout << "Exiting program.\n";
                break;

            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 4);

    return 0;
}
