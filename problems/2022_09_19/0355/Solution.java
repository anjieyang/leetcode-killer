class Tweet {
    int userId;
    int tweetId;

    public Tweet(int userId, int tweetId) {
        this.userId = userId;
        this.tweetId = tweetId;
    }
}

class Twitter {
    HashMap<Integer, HashSet<Integer>> followList;
    ArrayList<Tweet> tweets;

    public Twitter() {
        followList = new HashMap<>();
        tweets = new ArrayList<>();
    }

    public void postTweet(int userId, int tweetId) {
        tweets.add(new Tweet(userId, tweetId));
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> feed = new ArrayList<>();
        for (int i = tweets.size() - 1; i >= 0; i--) {
            Tweet current = tweets.get(i);

            if (followList.getOrDefault(userId, new HashSet<Integer>()).contains(current.userId)
                    || userId == current.userId)
                feed.add(current.tweetId);
            if (feed.size() == 10)
                break;
        }
        return feed;
    }

    public void follow(int followerId, int followeeId) {
        HashSet<Integer> follow = followList.getOrDefault(followerId, new HashSet<Integer>());
        follow.add(followeeId);
        followList.put(followerId, follow);
    }

    public void unfollow(int followerId, int followeeId) {
        followList.getOrDefault(followerId, new HashSet<Integer>()).remove(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */