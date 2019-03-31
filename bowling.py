class InvalidFrame(Exception):
    """Subclass of Exception to be raised in case of a function requiring a valid frame while receiving an invalid frame"""
    pass

def is_valid_frame(frame):
    """returns true if a frame is valid; a valid frame"""
    # checks if frame is a list with two integer elements
    if isinstance(frame, list) and len(frame) == 2 and isinstance(frame[0], int) and isinstance(frame[1], int):
        # checks if elements in frame are within possible range 1-10
        if 0 <= frame[0] <= 10 and 0 <= frame[1] <= 10 and sum(frame) <= 10:
            return True
    return False
    

def is_strike(frame):
    """returns True, if given frame is considered a strike"""
    # throw Exception, if not a valid frame
    if not is_valid_frame(frame):
        raise InvalidFrame
    # check if strike
    if frame == [10,0]:
        return True
    return False
    

def is_spare(frame):
    """returns True, if given frame is considered a spare"""
    # throw Exception, if not a valid frame
    if not is_valid_frame(frame):
        raise InvalidFrame
    # check if spare
    elif not is_strike(frame) and sum(frame) == 10:
        return True
    return False

def calc_points(bowling_frames):
    """returns a list of integers containing the point sums calculated from a list of bowling frames (2-element lists)"""
    result = []
    # iterate through each given frame
    for index, frame in enumerate(bowling_frames):
        # if first frame, just add sum of frame as score
        if index == 0:
            result.append(sum(frame))
        # check for bonus shots
        elif index == 10:
            # in case of strike on frame prior to last frame, give bonus points
            if is_strike(bowling_frames[index-2]):
                result[index-2] += frame[0]
                result[index-1] += frame[0]
            # add extra shot score to last frame, instead of new frame
            result[index-1] += sum(frame)
        else:
            # if not first frame, add sum of frame to previous score sum
            result.append(result[index-1] + sum(frame))
            previous_frame = bowling_frames[index-1]
            # if previous frame was a strike, add sum of current frame to the previous and current score sums 
            if is_strike(previous_frame):
                result[index-1] += sum(frame)
                result[index] += sum(frame)
                # if there is a frame before the previous frame, and they're both strikes, add first throw score to all three frames
                if index > 1 and is_strike(bowling_frames[index-2]):
                    result[index-2] += frame[0]
                    result[index-1] += frame[0]
                    result[index] += frame[0]
            # if previous frame was a spare, only score of first throw of current frame to the previous and current score sums 
            elif is_spare(previous_frame):
                result[index-1] += frame[0]
                result[index] += frame[0]
    return result